class Matrix:
    def __init__(self, matrixVal):
        self.matrix = matrixVal


class Solution:
    def removeIslands(self, matrix):
        # Time O(n*m) || Space O(n*m)
        if not matrix:
            return matrix

        n = len(matrix)
        m = len(matrix[0])
        rangeVal = [0, m - 1, n - 1]
        resultMatrix = Matrix(matrix)
        for i in range(0, n):  # Time O(n*m)
            for j in range(0, m):
                if i in rangeVal or j in rangeVal:
                    if resultMatrix.matrix[i][j] == 1:
                        self.identifyBoundryIsland(i, j, resultMatrix, n, m)

        for i in range(0, n):  # Time O(n*m)
            for j in range(0, m):
                if resultMatrix.matrix[i][j] == 2:
                    resultMatrix.matrix[i][j] = 1
                elif resultMatrix.matrix[i][j] == 1:
                    resultMatrix.matrix[i][j] = 0
        return resultMatrix.matrix

    def identifyBoundryIsland(self, row, col, resultMatrix, n, m):
        # Space O(n*m)[recursive Call]

        if 0 <= row < n and 0 <= col < m and resultMatrix.matrix[row][col] == 1:
            resultMatrix.matrix[row][col] = 2

            self.identifyBoundryIsland(row + 1, col, resultMatrix, n, m)
            self.identifyBoundryIsland(row, col + 1, resultMatrix, n, m)
            self.identifyBoundryIsland(row - 1, col, resultMatrix, n, m)
            self.identifyBoundryIsland(row, col - 1, resultMatrix, n, m)

        return


if __name__ == "__main__":

    print(
        Solution().removeIslands(
            [
                [1, 0, 0, 0, 1, 0, 0, 0],
                [1, 0, 1, 0, 1, 0, 1, 0],
                [1, 1, 0, 1, 0, 0, 1, 0],
                [1, 1, 0, 1, 1, 0, 1, 0],
                [1, 0, 0, 0, 1, 0, 0, 0],
            ]
        )
    )
