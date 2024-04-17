class Solution:
    def threeNumberSum(self, array, targetSum):
        ## Time O(n^2) || Space O(n)
        if not array:
            return []

        res = []
        array.sort()
        for idx in range(0, len(array) - 2):

            left = idx + 1
            right = len(array) - 1

            while left < right:

                currSum = array[idx] + array[left] + array[right]
                if currSum > targetSum:
                    right -= 1
                elif currSum < targetSum:
                    left += 1
                else:
                    res.append([array[idx], array[left], array[right]])
                    right -= 1
                    left += 1

        return res


if __name__ == "__main__":

    print(Solution().threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
    print(Solution().threeNumberSum([8, 10, -2, 49, 14], 57))
