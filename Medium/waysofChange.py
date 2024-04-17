class Solution:
    def numberOfWaysToMakeChange(self, n, denoms):
        ## Time (nd) [n: no.of.amount; d: no.of.demons] || Space O(n)
        if n == 0:
            return 1

        dp = [0] * (n + 1)
        dp[0] = 1
        for change in denoms:
            for amount in range(1, len(dp)):

                if change <= amount:
                    dp[amount] += dp[amount - change]
        return dp[n]


if __name__ == "__main__":

    print(Solution().numberOfWaysToMakeChange(0, [2, 3, 4, 7]))
    print(Solution().numberOfWaysToMakeChange(6, [1, 5]))
