class Solution():
    def findClosestValueInBst(self, tree, target):
        
        def helper(tree, target, closest):
            currNode = tree
            while currNode is not None:
                if abs(currNode.value - target) < abs(closest - target):
                    closest = currNode.value
                    
                if currNode.value > target:
                    currNode = currNode.left
                elif currNode.value < target:
                    currNode = currNode.right
                else:
                    break 
            
            return closest
                

        return helper(tree, target, tree.value)


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

node = BST(10)
node.left = BST(5)
node.left.left = BST(2)
node.left.right = BST(4)
node.right = BST(12)

if __name__ == '__main__':
    print(Solution().findClosestValueInBst(node,15))


