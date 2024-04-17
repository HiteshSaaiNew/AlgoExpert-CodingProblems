class Solution:
    def generateDocument(self, characters, document):
        # Time: O(d * (c+d)) [d:document; c:characters]
        # Space: O(1)

        if characters and not document:
            return True

        for char in document:

            documentFrequency = self.charCount(char, document)  # O(d)
            charactersFrequency = self.charCount(char, characters)  # (c)
            if documentFrequency > charactersFrequency:
                return False

        return True

    def charCount(self, character, targetFile):

        frequency = 0
        for letter in targetFile:
            if letter == character:
                frequency += 1

        return frequency


if __name__ == "__main__":

    print(
        Solution().generateDocument(
            "Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"
        )
    )
    print(Solution().generateDocument("aheaollabbhb", "hello"))
    print(Solution().generateDocument("    ", "      "))
