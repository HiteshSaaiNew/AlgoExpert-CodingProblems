# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class treeInfo:
    def __init__(self):
        self.idxVal = 0


def reconstructBst(preOrderTraversalValues):
    # Time O(n) || Space O(n)
    if not preOrderTraversalValues:
        return None

    treeIdx = treeInfo()
    return reconstructBstHelper(
        float("-inf"), float("inf"), preOrderTraversalValues, treeIdx
    )


def reconstructBstHelper(lowerBound, upperBound, traversList, rootIdx):

    if len(traversList) == rootIdx.idxVal:
        return None

    rootVal = traversList[rootIdx.idxVal]
    if rootVal < lowerBound or rootVal >= upperBound:
        return None

    rootIdx.idxVal += 1
    leftSubtree = reconstructBstHelper(lowerBound, rootVal, traversList, rootIdx)
    rightSubtree = reconstructBstHelper(rootVal, upperBound, traversList, rootIdx)

    return BST(rootVal, leftSubtree, rightSubtree)
