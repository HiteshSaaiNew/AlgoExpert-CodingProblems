class Solution:
    def arrayOfProducts(self, array):

        # Time O(n) || Space O(n)
        if len(array) < 2:
            return array

        leftProduct = [1] * len(array)
        rightProduct = [1] * len(array)
        result = [1] * len(array)
        n = len(array)

        for i in range(0, n):
            if i == 0:
                leftProduct[i] = 1
            else:
                leftProduct[i] = array[i - 1] * leftProduct[i - 1]

        for j in reversed(range(0, n)):
            if j == len(array) - 1:
                rightProduct[j] = 1
            else:
                rightProduct[j] = array[j + 1] * rightProduct[j + 1]

        for i in range(0, n):
            currIdxProduct = leftProduct[i] * rightProduct[i]
            result[i] = currIdxProduct

        return result


if __name__ == "__main__":

    print(Solution().arrayOfProducts([5, 1, 4, 2]))
    print(Solution().arrayOfProducts([2]))
    print(Solution().arrayOfProducts([-1, -1, -1, -1]))
    print(Solution().arrayOfProducts([0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))