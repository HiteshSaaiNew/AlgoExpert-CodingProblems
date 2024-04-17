class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Do not edit the return statement of this method.
		currNode = self ## ROOT Node/Current Node
		while True:
			if value < currNode.value:
				if currNode.left is None:
					currNode.left = BST(value)
					break
				else:
					currNode = currNode.left
			else:
				if currNode.right is None:
					currNode.right = BST(value)
					break
				else:
					currNode = currNode.right
		return self
	
    def contains(self, value):
		currNode = self ## ROOT Node/Current Node
		while currNode is not None:
			if value > currNode.value:
				currNode = currNode.right
			elif value < currNode.value:
				currNode = currNode.left
			else:
				return True 
		return False
		
			
    def remove(self, value, parentNode = None):
        # Do not edit the return statement of this method.
		currNode = self
		while currNode is not None:
			if value < currNode.value:
				parentNode = currNode
				currNode = currNode.left
			elif value > currNode.value:
				parentNode = currNode
				currNode = currNode.right
			else:
				if currNode.left and currNode.right:
					currNode.value = currNode.right.minVal()
					currNode.right.remove(currNode.value, currNode)
				elif parentNode is None:
					if currNode.left:
						currNode.value = currNode.left.value
						currNode.right = currNode.left.right
						currNode.left = currNode.left.left

					elif currNode.right:
						currNode.value = currNode.right.value
						currNode.left = currNode.right.left
						currNode.right = currNode.right.right
					else:
						pass
				elif parentNode.left == currNode:
					parentNode.left = currNode.left if currNode.left is not None else currNode.right
				elif parentNode.right == currNode:
					parentNode.right = currNode.left if currNode.left is not None else currNode.right
				break
				
        return self
	
	def minVal(self):
		currNode = self
		while currNode.left is not None:
			currNode = currNode.left
		return currNode.value
