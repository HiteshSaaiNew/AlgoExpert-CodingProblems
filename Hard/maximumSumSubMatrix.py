class Solution:
    def maximumSumSubmatrix(self, matrix, size):
        ## Time O(n*m) || Space O(n*m)
        maxSum = float("-inf")
        sums = self.createSumMatrix(matrix)

        rowS, colS = size - 1, size - 1
        for row in range(rowS, len(matrix)):
            for col in range(colS, len(matrix[0])):
                total = sums[row][col]

                if row == rowS and col == colS:
                    maxSum = max(maxSum, sums[row][col])
                    continue

                isTouchTop = row - size < 0
                if not isTouchTop:
                    total -= sums[row - size][col]

                isTouchLeft = col - size < 0
                if not isTouchLeft:
                    total -= sums[row][col - size]

                TouchingLeftOrTop = isTouchLeft or isTouchTop
                if not TouchingLeftOrTop:
                    total += sums[row - size][col - size]

                maxSum = max(maxSum, total)

        return maxSum

    def createSumMatrix(self, matrix):
        sums = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]

        sums[0][0] = matrix[0][0]

        ## Sum of first Row
        for i in range(1, len(matrix[0])):
            sums[0][i] = sums[0][i - 1] + matrix[0][i]

        ## Sum of first Column
        for i in range(1, len(matrix)):
            sums[i][0] = sums[i - 1][0] + matrix[i][0]

        ## Sum of rest of the positions
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                subSums = (sums[i - 1][j] + sums[i][j - 1]) - sums[i - 1][j - 1]
                sums[i][j] = subSums + matrix[i][j]

        return sums


if __name__ == "__main__":

    print(
        Solution().createSumMatrix(
            [[5, 3, -1, 5], [-7, 3, 7, 4], [12, 8, 0, 0], [1, -8, -8, 2]]
        )
    )
