class Solution:
    def minNumberOfCoinsForChange(self, n, denoms):
        # Time O(nd) || Space O(n)
        if n == 0:
            return 0

        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for denom in denoms:
            for amount in range(1, len(dp)):
                if denom <= amount:
                    dp[amount] = min(dp[amount], 1 + dp[amount - denom])

        return -1 if dp[-1] == float("inf") else dp[-1]


if __name__ == "__main__":

    print(Solution().minNumberOfCoinsForChange(7, [2, 4]))
    print(Solution().minNumberOfCoinsForChange(135, [39, 45, 130, 40, 4, 1, 60, 75]))
