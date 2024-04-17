class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class isAncestor:
    def __init__(self):
        self.anAncestor = False


class Solution:
    def validateThreeNodes(self, nodeOne, nodeTwo, nodeThree):
        # Time O(h) || Space O(1)
        isNodeOneAncestor = isAncestor()
        isNodeThreeAncestor = isAncestor()
        self.checkAncestor(nodeOne, isNodeOneAncestor, nodeTwo)
        self.checkAncestor(nodeThree, isNodeThreeAncestor, nodeTwo)

        if not isNodeOneAncestor.anAncestor and not isNodeThreeAncestor.anAncestor:
            return False

        if isNodeOneAncestor.anAncestor and isNodeThreeAncestor.anAncestor:
            return False

        if not isNodeOneAncestor.anAncestor:
            isNodeTwoAncestor = isAncestor()
            self.checkAncestor(nodeTwo, isNodeTwoAncestor, nodeOne)
            return isNodeThreeAncestor.anAncestor and isNodeTwoAncestor.anAncestor

        elif not isNodeThreeAncestor.anAncestor:
            isNodeTwoAncestor = isAncestor()
            self.checkAncestor(nodeTwo, isNodeTwoAncestor, nodeThree)
            return isNodeOneAncestor.anAncestor and isNodeTwoAncestor.anAncestor

    def checkAncestor(self, node, res, checkVal):

        while node is not None and node is not checkVal:
            node = node.left if checkVal.value < node.value else node.right

        res.anAncestor = node is checkVal

        return res.anAncestor
