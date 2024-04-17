class Solution:
    def balancedBrackets(self, string):

        # Time O(n) || Space O(n)
        if not string:
            return True
        if len(string) == 1:
            return False

        validOpenBracket = ["(", "{", "["]
        validCloseBracket = ["}", "]", ")"]
        matchingBracket = {")": "(", "]": "[", "}": "{"}

        stack = []

        for char in string:
            if char in validOpenBracket:
                stack.append(char)
            elif char in validCloseBracket and len(stack) == 0:
                return False
            elif char in validCloseBracket:
                checkMatchingOpenBracket = matchingBracket[char]
                if checkMatchingOpenBracket == stack[-1]:
                    stack.pop()
                else:
                    return False

        return not stack


if __name__ == "__main__":

    print(
        Solution().balancedBrackets(
            "(((((({{{{{safaf[[[[[([)]safsafsa)]]]]]}}}gawga}}))))))"
        )
    )

    print(Solution().balancedBrackets("(agwgg)([ghhheah%&@Q])"))
