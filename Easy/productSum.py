class Solution:
    def productSum(self, array, Pcounter = 1):
    # Write your code here.
	
	# Time O(n) || Space O(d)	
        res = 0 
        for instant in array:
            if isinstance(instant, int):
                res += instant
            else:
                res += self.productSum(instant, Pcounter + 1)
                
        return res * Pcounter



if __name__ == "__main__":

    print(Solution().productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
    print(Solution().productSum([[[[[[[[5,[4]]]]]]]]]))
    print(Solution().productSum([[[[[[5]]]]]]))







