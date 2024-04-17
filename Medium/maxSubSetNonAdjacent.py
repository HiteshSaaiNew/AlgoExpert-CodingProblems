class Solution:

    ##SOLUTION 1:
    def maxSubsetSumNoAdjacent1(self, array):

        ## Time O(n^2) || Space O(1)
        if len(array) == 0:
            return 0
        if len(array) == 1:
            return array[0]
        if len(array) == 2:
            if array[0] > array[1]:
                return array[0]
            else:
                return array[1]

        for i in range(2, len(array)):

            max_val = self.helper(i - 2, array)
            array[i] = array[i] + max_val

        return max(array)

    def helper(self, endPos, array, maxVal=float("-inf")):

        for j in reversed(range(0, endPos + 1)):

            maxVal = max(maxVal, array[j])

        return maxVal

    def maxSubsetSumNoAdjacent2(self, array):

        ## Time O(n) || Space O(1)
        if len(array) == 0:
            return 0
        if len(array) == 1:
            return array[0]
        if len(array) == 2:
            if array[0] > array[1]:
                return array[0]
            else:
                return array[1]

        n = len(array)
        ## first: Non-adjacent Number
        ## second: Max Number(Get's Shifted to the most recent index)
        first = array[0]
        second = max(array[0], array[1])
        for i in range(2, n):

            maxSum = max(second, first + array[i])
            first = second
            second = maxSum

        return second


if __name__ == "__main__":

    print(Solution().maxSubsetSumNoAdjacent1([75, 105, 120, 75, 90, 135]))
    print(Solution().maxSubsetSumNoAdjacent2([10, 5, 20, 25, 15, 5, 5, 15]))
