class Solution:
    def minimumWaitingTime(self, queries):

        # Time O(nlogn) || Space O(1)
        queries.sort()

        totalMinimumWaitTime = 0
        currTaskTime = queries[0]
        for idx in range(1, len(queries)):

            totalMinimumWaitTime += currTaskTime
            currTaskTime += queries[idx]

        return totalMinimumWaitTime


if __name__ == "__main__":

    print("Minimum Wait Time achieved \n")
    print(Solution().minimumWaitingTime([3, 2, 1, 2, 6]), "\n")
    print("Minimum Wait Time achieved \n")
    print(Solution().minimumWaitingTime([5, 1, 4]))
