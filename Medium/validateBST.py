class Solution:
    def __init__(self):
        self.currVal = float("-inf")

    def validateBst1(self, tree):
        return self.helper(tree, float("-inf"), float("inf"))

    def helper(self, tree, minVal, maxVal):

        if tree is None:
            return True
        if tree.value < minVal or tree.value >= maxVal:
            return False
        leftIsValid = self.helper(tree.left, minVal, tree.value)
        return leftIsValid and self.helper(tree.right, tree.value, maxVal)

    def validateBst2(self, root):

        if root:
            self.validateBst2(root.left)
            if root.value >= self.currVal:
                self.currVal = root.value
            else:
                return False
            self.validateBst2(root.right)

        return True