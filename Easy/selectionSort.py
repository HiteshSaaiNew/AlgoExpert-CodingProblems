class Solution:
    def selectionSort(self, array):
    # Write your code here.
	
	# Best/Average/Worst: Time O(n^2) || Space O(1)
	
        if len(array) == 1 or not array:
            return array 
        
        for i in range(0, len(array)):
            
            min_index = i 
            for j in range(i+1, len(array)):
                
                if array[j] < array[min_index]:
                    min_index = j
            
            array[min_index], array[i] = array[i], array[min_index]
        
        return array


if __name__ == '__main__':

    print(Solution().selectionSort([66,22,4,1,2,23,15,7,6,2,8]))