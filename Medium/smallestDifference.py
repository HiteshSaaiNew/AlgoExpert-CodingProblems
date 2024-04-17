class Solution:
    def smallestDifference(self, arrayOne, arrayTwo):

        ## Time O(n logn + m logm) || Space O(1)

        if not arrayOne and arrayTwo:
            return []

        idxOne = 0
        idxTwo = 0
        minimum = float("inf")
        arrayOne.sort()
        arrayTwo.sort()
        res = []

        while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):

            valueOne = arrayOne[idxOne]
            valueTwo = arrayTwo[idxTwo]

            if valueOne < valueTwo:
                currDiff = valueTwo - valueOne
                idxOne += 1

            elif valueOne > valueTwo:
                currDiff = valueOne - valueTwo
                idxTwo += 1

            else:
                currDiff = valueOne - valueTwo
                idxOne += 1
                idxTwo += 1

            if currDiff < minimum:
                res = [valueOne, valueTwo]
                minimum = currDiff

        return res


if __name__ == "__main__":

    print(Solution().smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))

    print(
        Solution().smallestDifference([10, 0, 20, 25], [1005, 1006, 1014, 1032, 1031])
    )
