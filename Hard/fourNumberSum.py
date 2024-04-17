class Solution:

    ## SOLUTION 1:
    def fourNumberSum1(self, array, targetSum):
        # Time O(n^3) || Space O(n^2)
        if len(array) < 4:
            return []

        res = []
        array.sort()
        for i in range(0, len(array) - 3):
            for j in range(i + 1, len(array) - 2):
                left = j + 1
                right = len(array) - 1
                while left < right:
                    currSum = array[i] + array[j] + array[left] + array[right]
                    if currSum < targetSum:
                        left += 1
                    elif currSum > targetSum:
                        right -= 1
                    else:
                        res.append([array[i], array[j], array[left], array[right]])
                        left += 1
                        right -= 1
        return res

    ## SOLUTION 2: RECOMMENDED
    def fourNumberSum2(self, array, targetSum):
        # Average case: Time O(n^2) || Space O(n^2)
        # Worst case:Time O(n^3) || Space O(n^2)
        allPairSum = {}
        res = []
        for i in range(1, len(array) - 1):
            for j in range(i + 1, len(array)):
                currSum = array[i] + array[j]
                diff = targetSum - currSum
                if diff in allPairSum:
                    for pair in allPairSum[diff]:
                        res.append(pair + [array[i], array[j]])

            for k in range(0, i):
                currSum = array[k] + array[i]
                if currSum not in allPairSum:
                    allPairSum[currSum] = [[array[k], array[i]]]
                else:
                    allPairSum[currSum].append([array[k], array[i]])
        return res


if __name__ == "__main__":
    print(Solution().fourNumberSum1([1, 2, 3, 4, 5, -5, 6, -6], 5))
    print(Solution().fourNumberSum2([-10, -3, -5, 2, 15, -7, 28, -6, 12, 8, 11, 5], 20))