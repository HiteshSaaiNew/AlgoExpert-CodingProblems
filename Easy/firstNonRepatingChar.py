class Solution:
    def firstNonRepeatingCharacter(self, string):
        ## Time O(n) || Space O(1)
        if not string:
            return -1

        charCount = {}
        for idx in range(len(string)):
            char = string[idx]
            if char not in charCount:
                charCount[char] = [0, idx]
            else:
                count, _ = charCount[char]
                count += 1
                charCount[char] = [count, idx]

        for char in charCount:
            count, idx = charCount[char]
            if count != 0:
                continue
            else:
                return idx
        return -1


if __name__ == "__main__":
    print(Solution().firstNonRepeatingCharacter("abcdcaf"))