class Solution:
    def reverseWordsInString(self, string):
        # Time O(n) || Space O(n)
        if not string:
            return ""

        words = []
        currWord = ""

        for i in range(0, len(string)):
            currChar = string[i]
            if currChar != " ":
                currWord += currChar

            elif i == 0 and currChar == " ":
                words.append(currChar)
                currWord = ""

            elif i == len(string) - 1 and currChar == " ":
                words.append(currWord)
                words.append(" ")
                currWord = ""

            else:
                words.append(currWord)
                words.append(" ")
                currWord = ""

        if currWord is not None:
            words.append(currWord)

        res = ""
        for j in reversed(range(0, len(words))):
            res += words[j]

        return res


if __name__ == "__main__":

    print(Solution().reverseWordsInString("Hitesh The Great!"))

    print(Solution().reverseWordsInString("124123 adsjfbskdjbf 123423 sdfnskjdnf "))