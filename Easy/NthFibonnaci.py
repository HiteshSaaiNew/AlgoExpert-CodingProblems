class Solution:

    def getNthFibSolution1(self, n, memo= {1:0, 2:1}):
    # Write your code here.

	# Time O(n) || Space O(n)

        if n in memo:
            return memo[n]
        else:
            memo[n] = self.getNthFibSolution1(n-1, memo) + self.getNthFibSolution1(n-2, memo)
        
        return memo[n]


    def getNthFibSolution2(self, n):

        # Write your code here.
        # O(n) Time || O(1) Space

        lastTwo = [0,1]
        counter = 2
        
        while counter < n:
            curr = sum(lastTwo)
            lastTwo[0], lastTwo[1] = lastTwo[1], curr
            counter += 1
        
        return lastTwo[1] if n > 1 else lastTwo[0]



if __name__ == "__main__":

    print(Solution().getNthFibSolution1(4))
    print(Solution().getNthFibSolution2(5))