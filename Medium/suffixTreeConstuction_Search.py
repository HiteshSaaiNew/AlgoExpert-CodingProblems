class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # Time O(n^2) Time || Space O(n^2)
    def populateSuffixTrieFrom(self, string):
        for i in range(0, len(string)):
            currNode = self.root
            for j in range(i, len(string)):
                currLetter = string[j]
                if currLetter not in currNode:
                    currNode[currLetter] = {}
                currNode = currNode[currLetter]
            currNode[self.endSymbol] = True

    #  Time O(m) || Space O(1); m - length of the search string
    def contains(self, string):
        currNode = self.root
        for letter in string:
            if letter in currNode:
                currNode = currNode[letter]
            else:
                return False

        return self.endSymbol in currNode


if __name__ == "__main__":

    # suffixTree = SuffixTrie("babc")

    print(SuffixTrie("babc").contains("bc"))
    print(SuffixTrie("babc").contains("cb"))
