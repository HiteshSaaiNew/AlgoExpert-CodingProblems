class Solution:
    def largestRange(self, array):
        ## Time O(n) || Space O(1)
        maxRangeLen = float("-inf")
        visited = {}
        for num in array:
            if num not in visited:
                visited[num] = True

        for num in array:
            if visited[num]:
                visited[num] = False

                leftVal = num - 1
                while leftVal in visited:
                    visited[leftVal] = False
                    leftVal -= 1

                rightVal = num + 1
                while rightVal in visited:
                    visited[rightVal] = False
                    rightVal += 1

                currMaxRangeLen = abs(leftVal - rightVal)
                if currMaxRangeLen > maxRangeLen:
                    maxRangeLen = currMaxRangeLen
                    res = [leftVal + 1, rightVal - 1]

        return res


if __name__ == "__main__":

    print(Solution().largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))
    print(Solution().largestRange([8, 4, 2, 10, 3, 6, 7, 9, 1]))