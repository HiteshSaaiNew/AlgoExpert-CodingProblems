class Solution:

    ## SOLUTION 1:
    def threeNumberSort1(self, array, order):
        ## Time O(3n) [order is constant with len. of 3] || Space O(1)
        if not order:
            return array

        leftPtr = 0
        for orderedNum in order:
            rightPtr = leftPtr + 1
            while rightPtr < len(array):
                if array[leftPtr] == orderedNum:
                    leftPtr += 1
                    rightPtr += 1
                elif array[leftPtr] != orderedNum and array[rightPtr] == orderedNum:
                    array[leftPtr], array[rightPtr] = array[rightPtr], array[leftPtr]
                    leftPtr += 1
                    rightPtr += 1
                else:
                    rightPtr += 1
        return array

    ## SOLUTION 2:
    def threeNumberSort2(self, array, order):
        # Time O(n) || Space O(1)
        if len(order) < 3 or not order:
            return array

        firstValue = order[0]
        thirdValue = order[2]

        firstIdx = 0
        for idx in range(len(array)):
            if array[idx] == firstValue:
                array[idx], array[firstIdx] = array[firstIdx], array[idx]
                firstIdx += 1

        thirdIdx = len(array) - 1
        for idx in reversed(range(len(array))):
            if array[idx] == thirdValue:
                array[idx], array[thirdIdx] = array[thirdIdx], array[idx]
                thirdIdx -= 1

        return array


if __name__ == "__main__":

    print(Solution().threeNumberSort1([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1]))
    print(Solution().threeNumberSort2([1, 0, 0, -1, -1, 0, 1, 1], [-1, 0, 1]))
