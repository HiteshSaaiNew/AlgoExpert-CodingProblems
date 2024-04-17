class Solution:
    def moveElementToEnd(self, array, toMove):

        # Time O(n) || Space O(1)
        if not array or len(array) == 1:
            return array

        left = 0
        right = 1

        while right < len(array):

            if array[left] == toMove and array[right] != toMove:
                array[left], array[right] = array[right], array[left]
                left += 1
                right += 1

            elif array[left] != toMove:
                left += 1
                right += 1

            else:
                right += 1

        return array


if __name__ == "__main__":

    print(Solution().moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))
    print(Solution().moveElementToEnd([1, 2, 4, 5, 6], 3))
    print(Solution().moveElementToEnd([3, 1, 3, 4, 5], 3))
