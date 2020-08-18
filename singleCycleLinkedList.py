# coding:utf-8

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class SingleCycleLinkedList(object):
    '''
    单向循环链表
    is_empty():判断链表是否为空
    length():返回链表长度
    travel():遍历整个链表
    add(item):头插法
    append(item):尾插法
    insert(pos, item):指定位置插入元素
    remove(item):删除节点
    search(item):查找节点是否存在
    '''
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.val, end=' ')
            cur = cur.next
        print(cur.val)

    def add(self, item):
        node = ListNode(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = node

    def append(self, item):
        node = ListNode(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                pre = pre.next
            node = ListNode(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.val == item:
                # 先判断此节点是否是头节点
                if cur == self.__head:
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环，cur指向尾结点
        if cur.val == item:
            if cur == self.__head:
                self.__head = None
            else:
                pre.next = cur.next

    def search(self, item):
        cur = self.__head
        while cur.next != self.__head:
            if cur.val == item:
                return True
            else:
                cur = cur.next
        if cur.val == item:
            return True
        return False

if __name__ == '__main__':
    ll = SingleCycleLinkedList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    # 8 1 2 3 4 5 6
    ll.insert(-1, 9)  # 9 8 1 2 3 4 5 6
    ll.travel()
    ll.insert(2, 100)  # 9 8 100 1 2 3 4 5 6
    ll.travel()
    ll.insert(10, 200)  # 9 8 100 1 2 3 4 5 6 200
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()