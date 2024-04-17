class Solution:
    def sunsetViews(self, buildings, direction):
        # Time O(n) || Space O(n)
        if not buildings:
            return []

        res = []
        if direction == "EAST":
            return self.helperSunsetEast(buildings, res)[::-1]
        else:
            return self.helperSunsetWest(buildings, res)

    def helperSunsetEast(self, buildings, res):
        runningMax = -1
        for i in reversed(range(0, len(buildings))):
            currBuildingHeight = buildings[i]
            if currBuildingHeight > runningMax:
                res.append(i)

            runningMax = max(runningMax, currBuildingHeight)

        return res

    def helperSunsetWest(self, buildings, res):
        runningMax = -1
        for i in range(0, len(buildings)):
            currBuildingHeight = buildings[i]
            if currBuildingHeight > runningMax:
                res.append(i)

            runningMax = max(runningMax, currBuildingHeight)

        return res


if __name__ == "__main__":

    print(Solution().sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], "EAST"))
    print(
        Solution().sunsetViews([1, 2, 3, 1, 5, 6, 9, 1, 9, 9, 11, 10, 9, 12, 8], "WEST")
    )
