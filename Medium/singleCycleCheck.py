class Solution:
    def hasSingleCycle(self, array):

        ## Time O(n) || Space O(1)
        if len(array) == 1:
            return True
        currentIdx = 0
        numOfElements = 0
        while numOfElements < len(array):
            if numOfElements > 0 and currentIdx == 0:
                return False
            numOfElements += 1
            currentIdx = self.getNextIdx(currentIdx, array)
        return currentIdx == 0

    def getNextIdx(self, idx, array):
        jump = array[idx]

        nextIdx = (idx + jump) % len(array)

        if nextIdx >= 0:
            return nextIdx
        else:
            return nextIdx + len(array)


if __name__ == "__main__":

    print(Solution().hasSingleCycle([[2, 3, 1, -4, -4, 2]]))
    print(Solution().hasSingleCycle([10, 11, -6, -23, -2, 3, 88, 908, -26]))
    print(Solution().hasSingleCycle([1, -1, 1, -1]))
