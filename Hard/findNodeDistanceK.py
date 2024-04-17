from collections import deque

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def findNodesDistanceK(self, tree, target, k):
        ## Time O(n) || Space O(n)
        parentNodes = {}
        self.getParentNodes(tree, parentNodes, None)
        targetNode = self.getNodeInfoTarget(tree, target, parentNodes)

        return self.BstOnNodesDistanceK(targetNode, parentNodes, k)

    def BstOnNodesDistanceK(self, targetNode, parentNodes, k):

        queue = deque([(targetNode, 0)])
        visited = {targetNode.value}
        while queue:

            currNode, currDistance = queue.popleft()

            if currDistance == k:
                resultNodes = [node.value for node, _ in queue]
                resultNodes.append(currNode.value)
                return resultNodes

            else:
                connectedNodes = [
                    currNode.left,
                    currNode.right,
                    parentNodes[currNode.value],
                ]

                for node in connectedNodes:
                    if node and node.value not in visited:
                        queue.append((node, currDistance + 1))
                        visited.add(node.value)

        return []

    def getNodeInfoTarget(self, node, target, parentNodes):
        if node.value == target:
            return node

        parent = parentNodes[target]

        if parent.left is not None and parent.left.value == target:
            return parent.left

        return parent.right

    def getParentNodes(self, node, parentNodes, parent):

        if node is not None:
            parentNodes[node.value] = parent
            self.getParentNodes(node.left, parentNodes, node)
            self.getParentNodes(node.right, parentNodes, node)
