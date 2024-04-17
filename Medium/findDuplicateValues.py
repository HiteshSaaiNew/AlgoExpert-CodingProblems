class Solution:
    def firstDuplicateValue(self, array):
        # Time O(n) || Space O(1)
        if not array or len(array) == 1:
            return -1

        for value in array:
            valueOfIdx = abs(value)
            if array[valueOfIdx - 1] < 0:
                return valueOfIdx
            else:
                array[valueOfIdx - 1] = -array[valueOfIdx - 1]

        return -1


if __name__ == "__main__":

    print(Solution().firstDuplicateValue([2, 3, 5, 1, 6, 2, 4]))
    print(Solution().firstDuplicateValue([2, 3, 5, 1, 3, 2, 4]))
