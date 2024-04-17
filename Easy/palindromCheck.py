class Solution:
    def isPalindrome(self, string):
        # Write your code here.

        # Time O(n) || Spcae O(1)

        if len(string) == 1:
            return True

        left = 0
        right = len(string) - 1

        while left <= right:

            if string[left] == string[right]:

                left += 1
                right -= 1

            else:

                return False

        return True


if __name__ == "__main__":

    print(Solution().isPalindrome("aabbaa"))
    print(Solution().isPalindrome("ab"))