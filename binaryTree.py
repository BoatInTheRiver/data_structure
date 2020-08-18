# coding:utf-8
from collections import deque

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

class Tree(object):
    '''
    二叉树
    add(item):往二叉树上加一个节点，满足完全二叉树
    levelOrder1(root):层序遍历
    levelOrder2(root):层序遍历
    preorder1(root):先序遍历--递归版
    inorder1(root):中序遍历--递归版
    postorder1(root):后续遍历--递归版
    preorder2(root):先序遍历--迭代版
    inorder2(root):中序遍历--迭代版
    postorder2(root):后续遍历--迭代版
    '''
    def __init__(self):
        self.root = None

    def add(self, item):
        node = TreeNode(item)
        if not self.root:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if not cur_node.left:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)
            if not cur_node.right:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)

    def levelOrder1(self, root):
        if not root:
            return
        res = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res

    def levelOrder2(self, root):
        '''之字型层序遍历'''
        if not root:
            return
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            tmp = deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if len(res) % 2 == 1:
                    tmp.appendleft(node.val)
                else:
                    tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(list(tmp))
        return res

    def preorder1(self, root):
        '''先序，递归版'''
        res = []
        def dfs(node):
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res

    def preorder2(self, root):
        '''先序，迭代版，借助栈'''
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if not node:
                continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))
                stack.append((GRAY, node))
            else:
                res.append(node.val)
        return res

    def inorder1(self, root):
        '''中序，递归版'''
        res = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res

    def inorder2(self, root):
        '''中序，迭代版，借助栈'''
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if not node:
                continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res

    def postorder1(self, root):
        '''后序，递归版'''
        res = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res

    def postorder2(self, root):
        '''后序，迭代版，借助栈'''
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if not node:
                continue
            if color == WHITE:
                stack.append((GRAY, node))
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res

if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    print(tree.levelOrder1(tree.root))
    print(tree.levelOrder2(tree.root))
    print('--------------')
    print(tree.preorder1(tree.root))
    print(tree.preorder2(tree.root))
    print('--------------')
    print(tree.inorder1(tree.root))
    print(tree.inorder2(tree.root))
    print('--------------')
    print(tree.postorder1(tree.root))
    print(tree.postorder2(tree.root))