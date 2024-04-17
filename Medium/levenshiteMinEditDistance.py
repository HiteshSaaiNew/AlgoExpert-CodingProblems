class Solution:
    def levenshteinDistance(self, str1, str2):
        # Time O(nm) || Space O(nm)
        n = len(str1)
        m = len(str2)
        if not str1 and str2:
            return m

        if str1 and not str2:
            return n

        edits = [[x for x in range(0, m + 1)] for y in range(0, n + 1)]

        for i in range(1, n + 1):
            edits[i][0] = edits[i - 1][0] + 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    edits[i][j] = edits[i - 1][j - 1]
                else:
                    edits[i][j] = 1 + min(
                        edits[i - 1][j - 1], edits[i - 1][j], edits[i][j - 1]
                    )

        return edits[-1][-1]


if __name__ == "__main__":

    print(Solution().levenshteinDistance("abc", "yabc"))
    print(Solution().levenshteinDistance("abc", "abcx"))
    print(Solution().levenshteinDistance("abcd", "ab"))
