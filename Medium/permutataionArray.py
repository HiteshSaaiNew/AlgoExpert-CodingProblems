class Solution:
    def getPermutations(self, array):
        # Time O(n*n!) || Space O(n*n!)

        res = []
        self.helperPermutation(array, [], res)
        return res

    def helperPermutation(self, array, currPermutation, res):
        if not array and currPermutation:
            res.append(currPermutation)

        for idx in range(len(array)):
            reminingArray = array[:idx] + array[idx + 1 :]
            newPermutation = currPermutation + [array[idx]]
            self.helperPermutation(reminingArray, newPermutation, res)


if __name__ == "__main__":

    print(Solution().getPermutations([1, 2, 3]))