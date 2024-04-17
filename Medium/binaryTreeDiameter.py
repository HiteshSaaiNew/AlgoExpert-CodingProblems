class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Time O(n) || Space O(n)
    if tree:
        return getTreeInfo(tree).diameter


def getTreeInfo(node):

    if not node:
        return TreeInfo(0, 0)

    leftInfo = getTreeInfo(node.left)
    rightInfo = getTreeInfo(node.right)

    currTotalHeight = leftInfo.height + rightInfo.height
    currMaxDiameter = max(leftInfo.diameter, rightInfo.diameter)
    currMaxDiameter = max(currTotalHeight, currMaxDiameter)
    currTotalHeight = 1 + max(leftInfo.height, rightInfo.height)
    print(currMaxDiameter, currTotalHeight)
    return TreeInfo(currMaxDiameter, currTotalHeight)


class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height
