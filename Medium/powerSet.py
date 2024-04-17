class Solution:
    def powerset(self, array):
        # Time O(n*2^n) || Space O(n*2^n)
        if not array:
            return [[]]

        powerSet = [[]]

        for i in reversed(range(len(array))):
            for j in range(len(powerSet)):
                currSubset = powerSet[j]
                powerSet.append([array[i]] + currSubset)

        return powerSet


if __name__ == "__main__":

    print(Solution().powerset([1, 2, 3, 4]))
