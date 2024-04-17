class Solution:

	def __init__(self, value=0):
		self.total = value

    ##SOLUTION 1:
    def nodeDepths1(self, root):
        # Time O(n) || Sapce O(h)
        if not root:
            return 0 

        nodeDepthSum = 0 
        stack = [{"node": root, "level" :0}]
        while len(stack) > 0:
            curr_stack = stack.pop()
            node, depth  = curr_stack['node'], curr_stack['level']
            if node is None:
                continue
            nodeDepthSum += depth
            stack.append({"node": node.left, "level" : depth+1})
            stack.append({"node": node.right, "level": depth+1})

        return nodeDepthSum
    
    ##SOLUTION 2:
    def nodeDepths2(self, root, depthSum = 0):
    
        # Time O(n) || Sapce O(h)
        if not root:
            return 0

        return depthSum + self.nodeDepths2(root.left, depthSum+1) + self.nodeDepths2(root.right, depthSum+1)

    ##SOLUTION 3:
	def nodeDepths3(self, sroot):

        # Time O(n) || Sapce O(h)

		if not root:
			return 0
      
		def countDepth(node, level):

			self.total += level 
			if node.left:
			  countDepth(node.left, level+1)
			if node.right:
				countDepth(node.right,level+1)

			return 


		level = 0
		countDepth(root, level)

		return self.total
  
