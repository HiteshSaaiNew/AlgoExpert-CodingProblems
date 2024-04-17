class Solution:
    def maxPathSum(self, tree):
        # Time O(n) ||
        # Space
        ## Average Case: O(log(n)) [balanced Tree]
        ## Worst Case: O(n) [skewed Tree]
        if not tree:
            return 0

        _, maxSum = self.helperMax(tree)
        return maxSum

    def helperMax(self, node):
        if not node:
            return (0, float("-inf"))

        leftBranchSum, leftMaxSum = self.helperMax(node.left)
        rightBranchSum, rightMaxSum = self.helperMax(node.right)
        maxChildSum = max(leftBranchSum, rightBranchSum)

        value = node.value
        maxSumAsBranch = max(maxChildSum + value, value)
        maxSumAsNode = max(leftBranchSum + rightBranchSum + value, maxSumAsBranch)
        maxPathSum = max(leftMaxSum, rightMaxSum, maxSumAsNode)

        return (maxSumAsBranch, maxPathSum)
