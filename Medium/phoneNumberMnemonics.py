class mnemonicsDict:
    def __init__(self):
        self.mnemonicsDict = {
            "1": ["1"],
            "0": ["0"],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }


class Solution:
    def phoneNumberMnemonics(self, phoneNumber):
        ## Time O(4^n*n) Time || Space O(4^n*n)
        ## n - length of the phone number
        finalMnemonics = []

        dictVal = mnemonicsDict()
        self.helperPhoneNumber(0, phoneNumber, "", finalMnemonics, dictVal)
        return finalMnemonics

    def helperPhoneNumber(
        self, idx, phoneNumber, currMnemonics, finalMnemonics, dictVal
    ):

        if idx == len(phoneNumber):
            finalMnemonics.append(currMnemonics)
            return

        currNumber = phoneNumber[idx]
        letters = dictVal.mnemonicsDict[currNumber]
        for letter in letters:
            self.helperPhoneNumber(
                idx + 1, phoneNumber, currMnemonics + letter, finalMnemonics, dictVal
            )


if __name__ == "__main__":

    print(Solution().phoneNumberMnemonics("2310"))
    print(Solution().phoneNumberMnemonics("110"))
    print(Solution().phoneNumberMnemonics(""))
    print(Solution().phoneNumberMnemonics("999"))
