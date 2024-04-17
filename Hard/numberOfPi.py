class Solution:
    def numbersInPi(self, pi, numbers):
        ## Time () || Space O(n+m)
        numbersTable = {num: True for num in numbers}
        minSpaces = self.getMinSpaces(pi, numbersTable, {}, 0)
        return -1 if minSpaces == float("inf") else minSpaces

    def getMinSpaces(self, pi, numbersTable, cache, idx):

        if idx == len(pi):
            return -1
        if idx in cache:
            return cache[idx]

        minSpace = float("inf")
        for i in range(idx, len(pi)):
            currNumber = pi[idx : i + 1]
            if currNumber in numbersTable:
                currMinSpace = self.getMinSpaces(pi, numbersTable, cache, i + 1)
                minSpace = min(minSpace, currMinSpace + 1)

        cache[idx] = minSpace
        return cache[idx]


if __name__ == "__main__":

    print(
        Solution().numbersInPi(
            "3141592653589793238462643383279",
            [
                "314159265358979323846",
                "26433",
                "8",
                "3279",
                "314159265",
                "35897932384626433832",
                "79",
            ],
        )
    )
