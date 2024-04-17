class Solution:
    def staircaseTraversal(self, height, maxSteps):

        return self.helper(height, maxSteps, {0: 1, 1: 1})

    def helper(self, height, maxSteps, memo):
        ## Time O(n*k) || Space O(1)
        if height in memo:
            return memo[height]

        res = 0
        for i in range(1, min(height, maxSteps) + 1):

            res += self.helper(height - i, maxSteps, memo)
        memo[height] = res

        return res


if __name__ == "__main__":

    print(Solution().staircaseTraversal(10, 4))