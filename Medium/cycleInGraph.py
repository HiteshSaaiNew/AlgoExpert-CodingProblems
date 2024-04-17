class Solution:
    def cycleInGraph(self, edges):
        # Time O(v+e) || Space O(v)
        if not edges:
            return False

        numberOfEdges = len(edges)
        visited = [0] * numberOfEdges
        inStack = [0] * numberOfEdges

        for i in range(len(edges)):

            if self.checkCycleInGraph(edges, i, visited, inStack):
                return True

        return False

    def checkCycleInGraph(self, edges, currNode, visited, inStack):

        visited[currNode] = 1
        inStack[currNode] = 1

        neighbors = edges[currNode]
        for neighbor in neighbors:
            if visited[neighbor] != 1:
                isThereCycle = self.checkCycleInGraph(edges, neighbor, visited, inStack)
                if isThereCycle:
                    return True
            elif inStack[neighbor] == 1:
                return True

        inStack[currNode] = False
        return False


if __name__ == "__main__":

    print(Solution().cycleInGraph([[1, 3], [2, 3, 4], [0], [], [2, 5], []]))
