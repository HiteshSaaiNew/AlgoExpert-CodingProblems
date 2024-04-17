class Solution:
    def groupAnagrams(self, words):

        # Time O(n*w*26) || Space O(n+26) -> O(n)  w = length of the words;
        # ------------------------------   n = length of the array

        if not words:
            return []
        if len(words) == 1:
            return [words]

        anagramGroup = {}
        res = []
        for word in words:  # Time O(n)
            wordCount = [0] * 26  # Space O(26)
            for letter in word:  # Time O(w)
                wordCount[ord(letter) - ord("a")] += 1

            wordCount = str(wordCount)  # Time O(26)
            if wordCount not in anagramGroup:
                anagramGroup[wordCount] = []

            anagramGroup[wordCount].append(word)

        for key in anagramGroup.keys():  # Time O(n)
            res.append(anagramGroup[key])  # Space O(n) [worst Case]

        return res


if __name__ == "__main__":

    print(
        Solution().groupAnagrams(
            ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
        )
    )
    print(Solution().groupAnagrams([]))
