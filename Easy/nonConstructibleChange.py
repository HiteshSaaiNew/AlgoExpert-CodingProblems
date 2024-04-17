class Solution:
    def nonConstructibleChange(self, coins):
        ## Time O(n) || Space O(1)

        if not coins:
            return 1

        coins.sort()
        currChange = 0

        for coin in coins:
            if coin > currChange + 1:
                return currChange + 1
            else:
                currChange += coin

        return currChange + 1


if __name__ == "__main__":

    print(Solution().nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]))
    print(Solution().nonConstructibleChange([1, 5, 1, 1, 1, 10, 15, 20, 100]))
