class Solution:
    def zigzagTraverse(self, array):
        ## Time O(n) || Space O(n)
        height = len(array)
        width = len(array[0])
        res = []
        isDown = True
        row = 0
        col = 0
        while self.inBoundry(row, col, height, width):
            res.append(array[row][col])
            if isDown:
                if col == 0 or row == height - 1:
                    isDown = False
                    if row == height - 1:
                        col += 1
                    else:
                        row += 1
                else:
                    row += 1
                    col -= 1
            else:
                if row == 0 or col == width - 1:
                    isDown = True
                    if col == width - 1:
                        row += 1
                    else:
                        col += 1
                else:
                    row -= 1
                    col += 1

        return res

    def inBoundry(self, row, col, height, width):

        return (0 <= row < height) and (0 <= col < width)


if __name__ == "__main__":

    print(
        Solution().zigzagTraverse(
            [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]
        )
    )
