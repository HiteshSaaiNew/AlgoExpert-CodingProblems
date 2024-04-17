class Solution:
    def sameBsts(self, arrayOne, arrayTwo):
        ## Time O(n^2) || Space o(n^2)
        if len(arrayOne) != len(arrayTwo):
            return False

        if len(arrayOne) == 0 and len(arrayTwo) == 0:
            return True

        if arrayOne[0] != arrayTwo[0]:
            return False

        leftOne, rightOne = self.helperListGen(arrayOne[0], arrayOne)
        leftTwo, rightTwo = self.helperListGen(arrayTwo[0], arrayTwo)

        left = self.sameBsts(leftOne, leftTwo)
        right = self.sameBsts(rightOne, rightTwo)

        return left and right

    def helperListGen(self, root, array):

        lstLeft = []
        lstRight = []

        for i in range(1, len(array)):
            if array[i] < root:
                lstLeft.append(array[i])

            elif array[i] >= root:
                lstRight.append(array[i])

        return lstLeft, lstRight


if __name__ == "__main__":

    print(
        Solution().sameBsts(
            [10, 15, 8, 12, 94, 81, 5, 2, 11], [10, 8, 5, 15, 2, 12, 11, 94, 81]
        )
    )
