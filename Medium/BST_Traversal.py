class Solution:
    def inOrderTraverse(self, tree, array):
        if tree:
            self.inOrderTraverse(tree.left, array)
            array.append(tree.value)
            self.inOrderTraverse(tree.right, array)

        return array

    def preOrderTraverse(self, tree, array):
        # Write your code here.
        if tree:
            array.append(tree.value)
            self.preOrderTraverse(tree.left, array)
            self.preOrderTraverse(tree.right, array)

        return array

    def postOrderTraverse(self, tree, array):
        # Write your code here.
        if tree:
            self.postOrderTraverse(tree.left, array)
            self.postOrderTraverse(tree.right, array)
            array.append(tree.value)

        return array