class Solution:
    def __init__(self):
        self.islandLen = 0

        ## SOLUTION 1:

    def riverSizes1(self, matrix):
        ## Time O(n*m) || Space O(n*m)
        n = len(matrix)
        m = len(matrix[0])

        res = []

        for i in range(0, n):
            for j in range(0, m):
                if matrix[i][j] == 1:
                    self.islandLen = 0
                    self.dfs(matrix, i, j)
                    res.append(self.islandLen)

        return res

    def dfs(self, matrix, row, col):

        if (
            0 <= row < len(matrix)
            and 0 <= col < len(matrix[0])
            and matrix[row][col] == 1
        ):
            matrix[row][col] = 0
            self.islandLen += 1
            self.dfs(matrix, row, col + 1)
            self.dfs(matrix, row, col - 1)
            self.dfs(matrix, row + 1, col)
            self.dfs(matrix, row - 1, col)

        return

        ######SOLUTION 2:
        # def riverSizes2(self, matrix):
        #     ## Time O(n*m) || Space O(n*m)
        #     sizes = []
        #     visited = [[False for value in row] for row in matrix]
        #     for i in range(len(matrix)):
        #         for j in range(len(matrix[i])):
        #             if visited[i][j]:
        #             continue
        #         self.traverseNode(i, j, matrix, visited, sizes)

        #     return sizes

        # def traverseNode(self, i, j , matrix, visited, sizes):
        #     currentRiverSize = 0
        #     nodesToExplore = [[i,j]]
        #     while len(nodesToExplore):
        #         currentNode = nodesToExplore.pop()
        #         i = currentNode[0]
        #         j = currentNode[1]
        #         if visited[i][j]:
        #             continue
        #         visited[i][j] = True
        #         if matrix[i][j] == 0:
        #             continue
        #         currentRiverSize += 1
        #         unvisitedNeighbors = self.getUnvisitedNeighbors(i, j , matrix, visited)
        #         for neighbor in unvisitedNeighbors:
        #             nodesToExplore.append(neighbor)
        #     if currentRiverSize > 0:
        #         sizes.append(currentRiverSize)

        # def getUnvisitedNeighbors(i, j, matrix, visited):
        #     unvisitedNeighbors = []
        #     if i > 0 and not visited[i-1][j]:
        #         self.unvisitedNeighbors.append([i-1, j])
        #     if i < len(matrix)-1 and not visited[i+1][j]:
        #         self.unvisitedNeighbors.append([i+1, j])
        #     if j > 0 and not visited[i][j-1]:
        #         self.unvisitedNeighbors.append([i, j-1])
        #     if j < len(matrix[0])-1 and not visited[i][j+1]:
        #         self.unvisitedNeighbors.append([i, j+1])

        #     return unvisitedNeighbors


if __name__ == "__main__":

    print(
        Solution().riverSizes1(
            [
                [1, 0, 0, 1, 0],
                [1, 0, 1, 0, 0],
                [0, 0, 1, 0, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 1, 1, 0],
            ]
        )
    )
