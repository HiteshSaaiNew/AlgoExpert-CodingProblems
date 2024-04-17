class Solution:
    def caesarCipherEncryptor(self, string, key):
        # Write your code here.

        # Time O(n) || Space O(n)
        if not string:
            return string

        total_moves = key % 26

        res = ""

        for letter in string:

            remining_moves = ((ord(letter) - 97) + total_moves) - 25

            if remining_moves <= 0:

                res += chr(ord(letter) + total_moves)

            else:
                res += chr(96 + (remining_moves))

        return res


if __name__ == "__main__":

    print(Solution().caesarCipherEncryptor("xyz", 4))
    print(Solution().caesarCipherEncryptor("suvs", 150))
    print(Solution().caesarCipherEncryptor("ade", 26))
    print(Solution().caesarCipherEncryptor("", 26))
