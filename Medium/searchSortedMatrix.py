class Solution:
    def searchInSortedMatrix1(self, matrix, target):
        # Time O(n+m) || Space O(1)
        if not len(matrix):
            return [-1, -1]

        row = 0
        col = len(matrix[0]) - 1

        while col >= 0 and row < len(matrix):
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1

            else:
                return [row, col]

        return [-1, -1]

    def searchInSortedMatrix2(self, matrix, target):
        # Time O(n+m) || Space O(1)
        if not len(matrix):
            return [-1, -1]

        row = len(matrix) - 1
        col = 0

        while row >= 0 and col < len(matrix[0]):

            if matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1

            else:
                return [row, col]

        return [-1, -1]


if __name__ == "__main__":

    print(
        Solution().searchInSortedMatrix1(
            [
                [1, 4, 7, 12, 15, 1000],
                [2, 5, 19, 31, 32, 1001],
                [3, 8, 24, 33, 35, 1002],
                [40, 41, 42, 44, 45, 1003],
                [99, 100, 103, 106, 128, 1004],
            ],
            44,
        )
    )

    print(
        Solution().searchInSortedMatrix2(
            [
                [1, 4, 7, 12, 15, 1000],
                [2, 5, 19, 31, 32, 1001],
                [3, 8, 24, 33, 35, 1002],
                [40, 41, 42, 44, 45, 1003],
                [99, 100, 103, 106, 128, 1004],
            ],
            12,
        )
    )

    print(
        Solution().searchInSortedMatrix2(
            [
                [1, 4, 7, 12, 15, 1000],
                [2, 5, 19, 31, 32, 1001],
                [3, 8, 24, 33, 35, 1002],
                [40, 41, 42, 44, 45, 1003],
                [99, 100, 103, 106, 128, 1004],
            ],
            22,
        )
    )
