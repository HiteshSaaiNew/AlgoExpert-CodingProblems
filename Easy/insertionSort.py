class Solution:
    def insertionSort(self, array):
        # Write your code here.
        
        # Best: Time O(n) || Space O(1)
        # Average/Worst: Time O(n^2) || Space O(1)
        if not array and len(array) == 1:
            return array
        
        n = len(array)
        
        for i in range(1, n):
            
            while array[i] < array[i-1] and i != 0:
                
                array[i], array[i-1] = array[i-1], array[i]
                
                i -= 1
        
        return array


if __name__ == "__main__":

    print(Solution().insertionSort([66,22,4,1,2,23,15,7,6,2,8]))


	
