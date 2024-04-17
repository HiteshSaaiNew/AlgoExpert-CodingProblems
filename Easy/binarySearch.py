class Solution():
    def binarySearch1(self, array, target):
        # Write your code here.
        
        ## METHOD 1:
        # Time O(n) || Space O(1)
        pointer = len(array)//2
        flagleft = 0
        flagright = 0
        while 0 <= pointer < len(array):
            
            if array[pointer] > target:
                flagleft = 1
                if not flagright:
                    pointer -= 1
                else:
                    return -1

            elif array[pointer] < target:
                flagright = 1
                if not flagleft:
                    pointer += 1
                else:
                    return -1
            
            else:
                return pointer
        
        return -1

    ## METHOD 2:
    # Time O(n) || O(1)
    def binarySearch2(self, array, target):
        # Write your code here.
        return self.helperBinarySearch(array, target, 0, len(array)-1)


    def helperBinarySearch(self, array, target, left, right):
        
        while left <= right: 
            middle = (left + right)//2
            currNum = array[middle]
            if target == currNum:
                return middle
            
            elif target < currNum:
                right = middle - 1
            
            elif target > currNum:
                left = middle + 1
        
        return -1 


			
if __name__ == "__main__":
    print(Solution().binarySearch1([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))
    print(Solution().binarySearch2([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 2))


		