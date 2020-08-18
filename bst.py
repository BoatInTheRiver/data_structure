class BiTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

class BST(object):
    '''二叉搜索树'''
    def __init__(self, li):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)

    def insert(self, node, val):
        if not node:
            node = BiTreeNode(val)
        elif val < node.val:
            node.left = self.insert(node.left, val)
            node.left.parent = node
        elif val > node.val:
            node.right = self.insert(node.right, val)
            node.right.parent = node
        return node

    def insert_no_rec(self, val):
        p = self.root
        if not p:
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.val:
                if p.left:
                    p = p.left
                else:
                    p.left = BiTreeNode(val)
                    p.left.parent = p
                    return
            elif val > p.val:
                if p.right:
                    p = p.right
                else:
                    p.right = BiTreeNode(val)
                    p.right.parent = p
                    return
            else:
                return

    def query(self, node, val):
        if not node:
            return None
        if node.val < val:
            return self.query(node.right, val)
        elif node.val > val:
            return self.query(node.left, val)
        else:
            return node

    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.val > val:
                p = p.left
            elif p.val < val:
                p = p.right
            else:
                return p
        return None

if __name__ == '__main__':
    tree = BST([4, 6, 7, 9, 2, 1, 3, 5, 8])
    print(tree.query_no_rec(7))
    print(tree.query_no_rec(10))