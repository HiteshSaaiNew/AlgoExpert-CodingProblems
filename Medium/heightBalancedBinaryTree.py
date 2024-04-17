# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self):
        self.isBalanced = True


class Solution:
    def heightBalancedBinaryTree(self, tree):
        # Time O(n) || Space O(n) n - number of nodes in the tree

        if not tree:
            return True
        treeInfo = TreeInfo()
        self.helper(tree, treeInfo)
        return treeInfo.isBalanced

    def helper(self, node, treeInfo):

        if not node:
            return 0

        leftH = self.helper(node.left, treeInfo)
        rightH = self.helper(node.right, treeInfo)

        if abs(leftH - rightH) > 1:
            treeInfo.isBalanced = False

        return max(leftH, rightH) + 1
