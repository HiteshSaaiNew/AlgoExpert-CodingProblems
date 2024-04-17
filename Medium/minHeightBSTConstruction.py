class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currNode = self
        while True:
            if value < currNode.value:
                if currNode.left is None:
                    currNode.left = BST(value)
                    break
                else:
                    currNode = currNode.left
            else:
                if currNode.right is None:
                    currNode.right = BST(value)
                    break
                else:
                    currNode = currNode.right


class Solution:

    ##SOLUTION 1:
    def minHeightBst1(self, array):
        # Time O(n) || Space O(n)
        return self.helperMinHeightBst1(array, None, 0, len(array) - 1)

    def helperMinHeightBst1(self, array, bst, startIdx, endIdx):
        if endIdx < startIdx:
            return

        midIdx = (startIdx + endIdx) // 2
        newNode = BST(array[midIdx])
        if not bst:
            bst = newNode
        else:
            if array[midIdx] < bst.value:
                bst.left = newNode
                bst = bst.left
            else:
                bst.right = newNode
                bst = bst.right
        self.helperMinHeightBst1(array, bst, startIdx, midIdx - 1)
        self.helperMinHeightBst1(array, bst, midIdx + 1, endIdx)
        return bst

    def minHeightBst2(self, array):
        # Time: O(n) || Space: O)(n)
        return self.helperMinHeightBst2(array, 0, len(array) - 1)

    def helperMinHeightBst2(self, array, startIdx, endIdx):
        if endIdx < startIdx:
            return

        midIdx = (startIdx + endIdx) // 2
        newNode = BST(array[midIdx])
        bst = newNode
        bst.left = self.helperMinHeightBst2(array, startIdx, midIdx - 1)
        bst.right = self.helperMinHeightBst2(array, midIdx + 1, endIdx)
        return bst

    def minHeightBst3(self, array):
        # Time O(nlog(n)) [because insert does log(n) operation] || Space O(n)
        return self.helperMinHeightBst3(array, None, 0, len(array) - 1)

    def helperMinHeightBst3(self, array, bst, startIdx, endIdx):
        if endIdx < startIdx:
            return

        midIdx = (startIdx + endIdx) // 2
        newVal = array[midIdx]
        if not bst:
            bst = BST(newVal)
        else:
            bst.insert(newVal)
        self.helperMinHeightBst3(array, bst, startIdx, midIdx - 1)
        self.helperMinHeightBst3(array, bst, midIdx + 1, endIdx)
        return bst
