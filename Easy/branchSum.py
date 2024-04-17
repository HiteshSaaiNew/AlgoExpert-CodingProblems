# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def branchSums(self, root):

        # O(n) Time || O(n) Space [At worst case for skewed tree (recusive call stack)]
        if root:
            res = []
            runningSum = 0
            self.helper(root, res, runningSum)

        return res

    def helper(self, node, res, runningSum):

        if node:
            runningSum += node.value

            if not node.left and not node.right:
                res.append(runningSum)

            if node.left:
                self.helper(node.left, res, runningSum)

            if node.right:
                self.helper(node.right, res, runningSum)
        else:
            return


tree = BinaryTree(1)
tree.left = BinaryTree(2)
tree.right = BinaryTree(3)
tree.right.left = BinaryTree(4)

if __name__ == "__main__":

    print(Solution().branchSums(tree))
    print(Solution().branchSums(BinaryTree(1)))
