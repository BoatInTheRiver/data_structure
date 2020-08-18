# coding:utf-8

class Stack(object):
    '''
    栈
    push(item):添加一个元素item到栈顶
    pop():弹出栈顶元素
    peek():返回栈顶元素
    is_empty():判断栈是否为空
    size():返回栈内元素个数
    '''
    def __init__(self):
        self.__list = []

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        return self.__list.pop()

    def peek(self):
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)


# 括号匹配
def brace_match(s):
    match = {'}':'{', ']':'[', ')':'('}
    stack = Stack()
    for ch in s:
        if ch in ('(', '[', '{'):
            stack.push(ch)
        else: # ch in (')', ']', '}')
            if stack.is_empty():
                return False
            elif stack.peek() == match[ch]:
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False

if __name__ == '__main__':
    # s = Stack()
    # s.push(1)
    # s.push(2)
    # s.push(3)
    # print(s.size())
    # s.push(4)
    # s.push(5)
    # print(s.pop())
    # print(s.pop())
    # print(s.pop())
    # print(s.pop())
    # print(s.pop())
    
    print(brace_match('[{()}(){[()]}({}){}]'))