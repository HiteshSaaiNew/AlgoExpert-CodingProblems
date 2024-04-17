class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


class Solution:
    def findSuccessor(self, stree, node):
        ## Time O(h) || Space O(1)
        if node.right:
            return self.leftMostChild(node.right)

        return self.rightMostChild(node)

    def leftMostChild(self, node):
        currNode = node
        while currNode.left:
            currNode = currNode.left

        return currNode

    def rightMostChild(self, node):
        currNode = node
        while currNode.parent is not None and currNode.parent.right == currNode:
            currNode = currNode.parent

        return currNode.parent