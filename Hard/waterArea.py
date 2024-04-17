class Solution:

    ##SOLUTION 1:
    def waterArea1(self, heights):
        # Time O(n) || Space O(n)
        maxes = [0 for x in heights]
        leftMax = 0
        for i in range(len(heights)):
            height = heights[i]
            currMax = max(height, leftMax)
            maxes[i] = leftMax
            leftMax = currMax

        rightMax = 0
        for j in reversed(range(len(heights))):
            height = heights[j]
            currMin = min(maxes[j], rightMax)
            if height < currMin:
                maxes[j] = currMin - height
            else:
                maxes[j] = 0

            rightMax = max(height, rightMax)

        return sum(maxes)

    ## SOLUTION 2:
    def waterArea2(self, heights):

        # Time O(n) || Space O(1)
        if len(heights) == 0:
            return 0

        leftIdx = 0
        rightIdx = len(heights) - 1
        leftMax = heights[leftIdx]
        rightMax = heights[rightIdx]
        surfaceArea = 0

        while leftIdx < rightIdx:
            if heights[leftIdx] < heights[rightIdx]:
                leftIdx += 1
                leftMax = max(heights[leftIdx], leftMax)
                surfaceArea += leftMax - heights[leftIdx]

            else:
                rightIdx -= 1
                rightMax = max(heights[rightIdx], rightMax)
                surfaceArea += rightMax - heights[rightIdx]

        return surfaceArea


if __name__ == "__main__":

    print(Solution().waterArea1([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))
    print(Solution().waterArea1([0, 1, 2, 1, 1]))
    print(Solution().waterArea2([0, 8, 0, 0, 10, 0, 0, 10, 0, 0, 1, 1, 0, 3]))