class Solution:
    def maxSumIncreasingSubsequence(self, array):
        ## Time O(n^2) || Space O(n)
        sequence = [None for i in array]
        sums = [num for num in array]
        maxSumIdx = 0
        for i in range(len(array)):
            currNum = array[i]
            for j in range(0, i):
                prevNum = array[j]
                if prevNum < currNum and sums[j] + currNum >= sums[i]:
                    sums[i] = sums[j] + currNum
                    sequence[i] = j
            if sums[i] >= sums[maxSumIdx]:
                maxSumIdx = i
        return [sums[maxSumIdx], self.buildSequence(array, maxSumIdx, sequence)]

    def buildSequence(self, array, maxSumIdx, sequence):

        res = []
        nextIdx = maxSumIdx

        while nextIdx is not None:
            res.append(array[nextIdx])
            nextIdx = sequence[nextIdx]

        return res[::-1]


if __name__ == "__main__":

    print(Solution().maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30]))