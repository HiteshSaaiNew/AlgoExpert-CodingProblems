class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:

    ##SOLUTION 1:
    def invertBinaryTree1(self, tree):
        # Time O(n) || Space O(n)
        if not tree:
            return
        queue = [tree]
        while len(queue):
            currNode = queue.pop(0)
            self.swap(currNode)
            if currNode.left:
                self.invertBinaryTree1(currNode.left)
            if currNode.right:
                self.invertBinaryTree1(currNode.right)
        return tree

    ##SOLUTION 2:
    def invertBinaryTree2(self, tree):
        # Time O(n) || Space O(n)
        queue = [tree]
        while len(queue):
            currNode = queue.pop(0)
            self.swap(currNode)
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)

    ##SOLUTION 3:
    def invertBinaryTree(self, tree):
        # Time O(n) || Spcae O(d)
        if not tree:
            return
        self.swap(tree)
        self.invertBinaryTree(tree.left)
        self.invertBinaryTree(tree.right)

        return tree

    def swap(self, node):
        node.left, node.right = node.right, node.left
