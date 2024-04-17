class Solution:
    def kadanesAlgorithm(self, array):
        # Time O(n) || Space O(1)
        runningMaxSum = array[0]
        finalMaxSum = array[0]

        for idx in range(1, len(array)):

            runningMaxSum = max(array[idx], array[idx] + runningMaxSum)
            finalMaxSum = max(finalMaxSum, runningMaxSum)

        return finalMaxSum


if __name__ == "__main__":

    print(
        Solution().kadanesAlgorithm(
            [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
        )
    )
    print(Solution().kadanesAlgorithm([-2, -1]))
    print(
        Solution().kadanesAlgorithm(
            [8, 5, -9, 1, 3, -2, 3, 4, 7, 2, -18, 6, 3, 1, -5, 6]
        )
    )
