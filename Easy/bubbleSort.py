class Solution:
    def bubbleSort(self, array):
        # Write your code here.
        
        # Best: Time O(n) || Space O(1)
        # Average/Worst: Time O(n^2) || Space O(1)
        
        if not array or len(array) == 1:
            return array
        
        n = len(array)
        
        for i in range(0, n):
            
            for j in range(0, n-i-1):
                
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                
        
        return array


if __name__ == "__main__":

    print(Solution().bubbleSort([2,1,5,3,11,6,15]))
	