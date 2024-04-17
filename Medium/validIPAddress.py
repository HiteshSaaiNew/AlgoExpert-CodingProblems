class Solution:
    def validIPAddresses(self, string):
        # Time O(1) || Space O(1)
        if not string:
            return []

        ipCombinations = []

        for i in range(0, 3):
            first = string[: i + 1]
            if not self.isValidString(first):
                continue
            for j in range(i + 1, i + 4):
                second = string[i + 1 : j + 1]
                if not self.isValidString(second):
                    continue
                for k in range(j + 1, j + 5):
                    third = string[j + 1 : k + 1]
                    fourth = string[k + 1 :]
                    if self.isValidString(third) and self.isValidString(fourth):
                        ipCombinations.append(
                            first + "." + second + "." + third + "." + fourth
                        )
        return ipCombinations

    def isValidString(self, string):
        if string:
            stringInt = int(string)
            if stringInt > 255:
                return False
            else:
                return len(string) == len(str(stringInt))
        else:
            return False


if __name__ == "__main__":
    print(Solution().validIPAddresses("94321596"))
    print(Solution().validIPAddresses("123456789"))
    print(Solution().validIPAddresses("124310132"))
