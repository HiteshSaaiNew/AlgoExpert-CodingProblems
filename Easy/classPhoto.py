class Solution:
    def classPhotos(self, redShirtHeights, blueShirtHeights):

        # Time O(nlog(n)) || Space O(1)
        redShirtHeights.sort()
        blueShirtHeights.sort()

        backRowColor = "RED" if redShirtHeights[0] >= blueShirtHeights[0] else "BLUE"
        for i in range(0, len(redShirtHeights)):

            redStudentHeight = redShirtHeights[i]
            blueStudentHeight = blueShirtHeights[i]

            if backRowColor == "RED":
                if blueStudentHeight >= redStudentHeight:
                    return False

            else:
                if redStudentHeight >= blueStudentHeight:
                    return False

        return True


if __name__ == "__main__":

    print(Solution().classPhotos([6, 9, 2, 4, 5, 1], [5, 8, 1, 3, 4, 9]))
    print(Solution().classPhotos([1, 1, 1, 1, 1, 1, 1, 1], [5, 6, 7, 2, 3, 1, 2, 3]))
    print(Solution().classPhotos([5, 8, 1, 3, 4], [6, 9, 2, 4, 5]))
