class Solution:
    def dijkstrasAlgorithm(self, start, edges):
        ## Time O(V*2 + e) || Space O(V)
        minDistance = [float("inf")] * len(edges)
        visited = set()

        minDistance[start] = 0

        while len(visited) != len(edges):

            vertex, currMinDistance = self.getVertexWithMinDistance(
                minDistance, visited
            )
            if currMinDistance == float("inf"):
                break

            visited.add(vertex)
            for edge in edges[vertex]:
                destination, destinationDistance = edge

                if destination in visited:
                    continue

                newPathDistance = currMinDistance + destinationDistance
                currPathDistance = minDistance[destination]
                if newPathDistance < currPathDistance:
                    minDistance[destination] = newPathDistance

        return list(map(lambda x: -1 if x == float("inf") else x, minDistance))

    def getVertexWithMinDistance(self, distances, visited):
        currDistance = float("inf")
        vertex = -1

        for vertexIdx, distance in enumerate(distances):

            if vertexIdx in visited:
                continue

            if distance <= currDistance:
                currDistance = distance
                vertex = vertexIdx

        return vertex, currDistance


if __name__ == "__main__":

    print(
        Solution().dijkstrasAlgorithm(
            0, [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]
        )
    )

    print(
        Solution().dijkstrasAlgorithm(
            4,
            [
                [[1, 3], [2, 2]],
                [[3, 7]],
                [[1, 2], [3, 4], [4, 1]],
                [],
                [[0, 2], [1, 8], [3, 1]],
            ],
        )
    )

    print(Solution().dijkstrasAlgorithm(1, [[[1, 2]], [[0, 1]], [[3, 1]], [[2, 2]]]))
