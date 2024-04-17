# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class count:
    def __init__(self):
        self.visitedCount = 0
        self.value = 0


class Solution:
    def findKthLargestValueInBst(self, tree, k):
        # O(h + k) Time || O(h) - where h is the height of the tree and k is the input value
        trackCount = count()
        self.helperKthLargest(tree, k, trackCount)
        return trackCount.value

    def helperKthLargest(self, node, k, trackCount):
        if not node or trackCount.visitedCount >= k:
            return

        self.helperKthLargest(node.right, k, trackCount)
        if trackCount.visitedCount < k:
            trackCount.value = node.value
            trackCount.visitedCount += 1
            self.helperKthLargest(node.left, k, trackCount)


if __name__ == "__main__":

    tree = BST(5)
    tree.left = BST(4)
    tree.right = BST(7)
    tree.right.left = BST(6)
    tree.right.right = BST(12)
    print(Solution().findKthLargestValueInBst(tree, 1))
    print(Solution().findKthLargestValueInBst(tree, 3))
    print(Solution().findKthLargestValueInBst(tree, 4))
