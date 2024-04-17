class Solution:
    def longestPalindromicSubstring(self, string):

        # Time O(n^3) || Space O(1)
        if len(string) == 1 or not string:
            return string

        maxLen = float("-inf")
        idxOfPalindrom = [None, None]  # Space O(2) --> Space O(1) [constant]

        ptr1 = 0
        ptr2 = 0

        for ptr1 in range(0, len(string)):  # Time O(n)
            for ptr2 in range(ptr1, len(string)):  # Time O(n) --> O(n*n)
                if string[ptr1] == string[ptr2]:
                    if self.checkPalindrom(ptr1, ptr2, string):
                        if maxLen < (ptr2 - ptr1) + 1:
                            maxLen = (ptr2 - ptr1) + 1
                            idxOfPalindrom = [ptr1, ptr2 + 1]

                    elif self.checkPalindrom(ptr1, ptr2, string):
                        if maxLen < (ptr2 - ptr1) + 1:
                            maxLen = (ptr2 - ptr1) + 1
                            idxOfPalindrom = [ptr1, ptr2 + 1]

        return string[idxOfPalindrom[0] : idxOfPalindrom[1]]

    def checkPalindrom(self, left, right, string):  # Time O(n)

        while left <= right:

            if string[left] == string[right]:
                left += 1
                right -= 1
            else:
                return False

        return True


if __name__ == "__main__":

    print(Solution().longestPalindromicSubstring("abaxyzzyxf"))
    print(Solution().longestPalindromicSubstring("noon high it is"))
    print(Solution().longestPalindromicSubstring(""))
    print(Solution().longestPalindromicSubstring("a"))
    print(Solution().longestPalindromicSubstring("zzzzzzz2345abbbba5432zzbbababa"))
