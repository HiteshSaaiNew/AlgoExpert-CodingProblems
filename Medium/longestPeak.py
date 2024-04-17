class Solution:
    ## Time O(n) || Space O(1)
    def longestPeak(self, array):
        # Write your code here.
        if len(array) < 3:
            return 0

        longestPeakLength = 0
        currPos = 1
        while currPos < len(array) - 1:
            prevVal = array[currPos - 1]
            nextVal = array[currPos + 1]
            if prevVal < array[currPos] > nextVal:

                leftPos = currPos - 1
                while leftPos > 0 and array[leftPos] > array[leftPos - 1]:
                    leftPos -= 1

                rightPos = currPos + 1
                while (
                    rightPos < len(array) - 1 and array[rightPos] > array[rightPos + 1]
                ):
                    rightPos += 1

                currPeakLength = (rightPos - leftPos) + 1
                longestPeakLength = max(longestPeakLength, currPeakLength)
                currPos = rightPos
            else:
                currPos += 1
                continue

        return longestPeakLength


if __name__ == "__main__":

    print(Solution().longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))
    print(Solution().longestPeak([]))
    print(
        Solution().longestPeak(
            [
                1,
                1,
                1,
                2,
                3,
                10,
                12,
                -3,
                -3,
                2,
                3,
                45,
                800,
                99,
                98,
                0,
                -1,
                -1,
                2,
                3,
                4,
                5,
                0,
                -1,
                -1,
            ]
        )
    )
