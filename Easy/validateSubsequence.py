class Solution:
    def isValidSubsequence(self, array, sequence):
        # Write your code here.
        if not array and sequence:
            return False

        if array and not sequence:
            return False

        currIndex = 0
        for num in array:

            if num == sequence[currIndex]:
                currIndex += 1

            if currIndex == len(sequence):
                break

        return currIndex == len(sequence)


if __name__ == "__main__":

    print(Solution().isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
    print(Solution().isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [-1, 1, 10]))
