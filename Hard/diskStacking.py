class Solution:
    def diskStacking(self, disks):
        ## Time O(n^2) || Space O(n)
        if not disks:
            return []

        disks.sort(key=lambda disk: disk[2])
        heights = [i[2] for i in disks]
        sequence = [None for i in range(len(disks))]
        maxIdx = 0
        for i in range(1, len(disks)):
            for j in range(0, i):
                currDisk = disks[i]
                otherDisk = disks[j]
                if self.isInOrder(currDisk, otherDisk):
                    if heights[i] <= currDisk[2] + heights[j]:
                        heights[i] = currDisk[2] + heights[j]
                        sequence[i] = j
            if heights[i] >= heights[maxIdx]:
                maxIdx = i

        return self.getTheSequence(sequence, disks, maxIdx)

    def getTheSequence(self, sequence, disks, maxIdx):
        res = []
        while sequence[maxIdx] is not None:
            res.append(disks[maxIdx])
            maxIdx = sequence[maxIdx]

        res.append(disks[maxIdx])
        return list(reversed(res))

    def isInOrder(self, cD, oD):
        if oD[0] < cD[0] and oD[1] < cD[1] and oD[2] < cD[2]:
            return True
        return False


if __name__ == "__main__":

    print(
        Solution().diskStacking(
            [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]
        )
    )
