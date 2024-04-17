class Solution():

    def findThreeLargestNumbers(self, array):
        # Write your code here.
        
        # Time O(n) || Space O(1)
        
        if len(array) < 3:
            return []

        threeLargest = [float('-inf')]*3
        
        res = self.helperThreeLargest(array, threeLargest)
        
        return res
	
    def helperThreeLargest(self, array, threeLargest):
        
        for element in array:
            
            if element > threeLargest[2]:
                self.swapeValues(element, threeLargest, 2 )
            
            elif element > threeLargest[1]:
                self.swapeValues(element, threeLargest, 1)
            
            elif element > threeLargest[0]:
                self.swapeValues(element, threeLargest, 0)
        
        return threeLargest


    def swapeValues(self, currNum, swapArray, idx):
        
        for i in range(0, idx+1):
            
            if i == idx:
                swapArray[i] = currNum
            
            else:
                swapArray[i] = swapArray[i+1]
        
        return swapArray
	
		
		
if __name__ == '__main__':

    print(Solution().findThreeLargestNumbers([2,5,1,7,11,8,2,20,5]))