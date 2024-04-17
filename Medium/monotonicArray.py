class Solution:

    ##SOLUTION 1:
    def isMonotonic1(self, array):

        # Time O(n) || Space O(1)
        if len(array) <= 2:
            return True

        flag = float("inf")
        for i in range(0, len(array) - 1):

            check = array[i + 1] - array[i]

            if check == 0:
                continue

            elif check > 0:
                if flag != float("inf") and flag < 0:
                    return False
                else:
                    flag = 1

            elif check < 0:
                if flag != float("inf") and flag > 0:
                    return False
                else:
                    flag = -1

        return True

    ##SOLUTION 2
    def isMonotonic2(self, array):

        # Time O(n) || Space O(1)
        if len(array) <= 2:
            return True

        diff = array[1] - array[0]
        for i in range(1, len(array) - 1):
            if diff == 0:
                diff = array[i + 1] - array[i]
                continue
            if self.checkMonotonic(diff, array[i], array[i + 1]):
                return False

        return True

    def checkMonotonic(self, diff, currVal, nextVal):
        currDiff = nextVal - currVal
        if diff > 0:
            return currDiff < 0
        return currDiff > 0

    ## SOLUTION 3:
    def isMonotonic3(self, array):
        # Time O(n) || Space O(1)
        if len(array) <= 2:
            return True

        nonDecreasing = True
        nonIncreasing = True
        for i in range(0, len(array) - 1):

            if array[i + 1] > array[i]:
                nonDecreasing = False

            if array[i + 1] < array[i]:
                nonIncreasing = False

        return nonDecreasing or nonIncreasing


if __name__ == "__main__":

    print(Solution().isMonotonic1([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))
    print(Solution().isMonotonic3([-1, -5, -10, -1100, -900, -1101, -1102, -9001]))
    print(Solution().isMonotonic2([1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11]))
