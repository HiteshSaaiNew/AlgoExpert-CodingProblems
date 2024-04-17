class Solution:

    ## SOLUTION 1
    def runLengthEncoding1(self, string):
        # Time O(n^2) [concatenating with + for string]
        # Space O(n)

        res = ""
        prevChar = string[0]
        wordCount = 1

        for i in range(1, len(string)):

            currChar = string[i]
            if currChar == prevChar:
                wordCount += 1

            else:
                if wordCount > 9:
                    res += ("9" + prevChar) * (wordCount // 9)
                    res += str(wordCount % 9) + prevChar

                else:
                    res += str(wordCount) + prevChar

                prevChar = currChar
                wordCount = 1

        ## Handling the last run.
        if wordCount > 9:
            res += ("9" + prevChar) * (wordCount // 9)
            res += str(wordCount % 9) + prevChar

        else:
            res += str(wordCount) + prevChar

        return res

    ## SOULTION 2
    def runLengthEncoding2(self, string):

        # Time O(n) || Space O(n)
        encodedString = []
        currentCount = 1

        for i in range(1, len(string)):

            currChar = string[i]
            prevChar = string[i - 1]

            if currChar != prevChar or currentCount == 9:

                encodedString.append(str(currentCount))
                encodedString.append(prevChar)
                currentCount = 0

            currentCount += 1

        encodedString.append(str(currentCount))
        encodedString.append(string[-1])

        return "".join(encodedString)


if __name__ == "__main__":

    print(Solution().runLengthEncoding1("AAAAAAAAAAAAABBCCCCDD"))
    print(Solution().runLengthEncoding2("AAAAAAAAAAAAABBCCCCDD"))