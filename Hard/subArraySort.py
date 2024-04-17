class Solution:
    def subarraySort(self, array):
        # Time O(n) || Space O(1)
        if len(array) < 2:
            return [-1, -1]

        minValUnsorted = float("inf")
        maxValUnsorted = float("-inf")

        for i in range(len(array) - 1):

            if array[i] <= array[i + 1]:
                continue
            elif array[i] > array[i + 1]:
                minValUnsorted = min(array[i], array[i + 1], minValUnsorted)
                maxValUnsorted = max(array[i], array[i + 1], maxValUnsorted)

        if minValUnsorted == float("inf"):
            return [-1, -1]

        else:
            startIdx = self.helperStartIdx(array, minValUnsorted)
            endIdx = self.helperEndIdx(array, maxValUnsorted)

        return [startIdx, endIdx]

    def helperStartIdx(self, array, minValUnsorted):
        startIdx = -1
        for i in range(len(array)):
            if array[i] <= minValUnsorted:
                continue
            else:
                startIdx = i
                break

        return startIdx

    def helperEndIdx(self, array, maxValUnsorted):
        endIdx = -1
        for i in reversed(range(len(array))):
            if array[i] >= maxValUnsorted:
                continue
            else:
                endIdx = i
                break
        return endIdx


if __name__ == "__main__":

    print(Solution().subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))
    print(Solution().subarraySort([4, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 11, 57]))