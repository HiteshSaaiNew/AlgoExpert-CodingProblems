class Solution:
    def knapsackProblem(self, items, capacity):
        # Write your code here.
        # return [
        #   10, // total value
        #   [1, 2], // item indices
        # ]
        ## Time O(n*c) || Space O(n*c)
        knapsack = [
            [0 for i in range(0, capacity + 1)] for y in range(0, len(items) + 1)
        ]
        for i in range(1, len(items) + 1):
            currWeight = items[i - 1][1]
            currValue = items[i - 1][0]
            for c in range(0, capacity + 1):
                if currWeight > c:
                    knapsack[i][c] = knapsack[i - 1][c]
                else:
                    knapsack[i][c] = max(
                        knapsack[i - 1][c], knapsack[i - 1][c - currWeight] + currValue
                    )

        return [knapsack[-1][-1], self.getKnapscakItems(knapsack, items)]

    def getKnapscakItems(self, knapsack, items):
        sequence = []
        i = len(knapsack) - 1
        j = len(knapsack[0]) - 1
        while i > 0:
            if knapsack[i - 1][j] != knapsack[i][j]:
                sequence.append(i - 1)
                j -= items[i - 1][1]
                i -= 1
            else:
                i -= 1

            if j == 0:
                break

        return list(reversed(sequence))