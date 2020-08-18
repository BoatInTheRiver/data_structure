# coding:utf-8

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class SingleLinkedList(object):
    '''
    单链表
    is_empty():检查链表是否为空
    length():返回链表长度
    travel():遍历整个链表
    add(item):链表头部添加元素
    append(item):链表尾部添加元素
    insert(pos, item):指定位置添加元素
    remove(item):删除指定节点
    search(item):查找节点是否存在
    '''
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        # cur用来遍历节点
        cur = self.__head
        # count用来记录数量
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur:
            print(cur.val, end=' ')
            cur = cur.next
        print('')

    def add(self, item):
        node = ListNode(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        node = ListNode(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            pre =  self.__head
            count = 0
            while count < pos - 1:
                count += 1
                pre = pre.next
            node = ListNode(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        cur = self.__head
        pre = None
        while cur:
            if cur.val == item:
                # 先判断此节点是否为头结点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        cur = self.__head
        while cur:
            if cur.val == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    ll = SingleLinkedList()
    print(ll.is_empty())
    print(ll.length())
    print('------------')
    ll.append(1)
    ll.append(2)
    ll.add(9)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.add(6)
    ll.append(7)
    print(ll.length())
    # 6 9 1 2 3 4 5 7
    ll.insert(-1, 8)    # 8 6 9 1 2 3 4 5 7
    ll.travel()
    ll.insert(13, 15)   # 8 6 9 1 2 3 4 5 7 15
    ll.travel()
    print('------------')
    ll.remove(15)   # 8 6 9 1 2 3 4 5 7
    ll.travel()
    print(ll.search(4)) # True