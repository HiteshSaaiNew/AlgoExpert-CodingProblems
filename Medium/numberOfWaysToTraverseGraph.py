class Solution:
    def numberOfWaysToTraverseGraph(self, width, height):
        # Time O(w*h) || Space O(w) w - width, h - height
        if width * height < 2:
            return 1

        dp = [0] * width
        dp[0] = 1

        for _ in range(height):
            for j in range(1, width):
                dp[j] = dp[j - 1] + dp[j]

        return dp[-1]


if __name__ == "__main__":

    print(Solution().numberOfWaysToTraverseGraph(2, 3))
    print(Solution().numberOfWaysToTraverseGraph(4, 3))
    print(Solution().numberOfWaysToTraverseGraph(1, 1))
