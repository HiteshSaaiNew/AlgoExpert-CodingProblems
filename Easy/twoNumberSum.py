
class Solution:
    def twoNumberSum(self, array, targetSum):
        # Write your code here.
        
        # Time O(nlogn) || Space O(1)
        if len(array) < 2:
            return []
        
        array.sort() #<---- nlogn
        
        left = 0 
        right = len(array)-1
        
        while left < right:
            
            curr_sum = array[left] + array[right]
            
            if curr_sum < targetSum:
                left += 1
            
            elif curr_sum > targetSum:
                right -= 1
                
            else:
                return [array[left], array[right]]
        
        return []

if __name__ == "__main__":

    print(Solution().twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))