class Solution:
    def minNumberOfJumps1(self, array):
        ## Time O(n^2) || Space o(n)
        jumps = [float("inf")] * len(array)
        jumps[0] = 0
        for i in range(1, len(array)):
            for j in range(0, i):
                if array[j] + j >= i:
                    jumps[i] = min(jumps[j] + 1, jumps[i])
        return jumps[-1]

    def minNumberOfJumps2(self, array):
        ## Time O(n) || Space O(1)
        if len(array) == 1:
            return 0
        maxReach = array[0]
        steps = array[0]
        jumps = 0
        for i in range(1, len(array) - 1):
            currReach = array[i] + i
            maxReach = max(maxReach, currReach)
            steps -= 1
            if steps == 0:
                jumps += 1
                steps = maxReach - i

        return jumps + 1


if __name__ == "__main__":
    print(Solution().minNumberOfJumps1([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]))
    print(
        Solution().minNumberOfJumps1(
            [3, 12, 2, 1, 2, 3, 15, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1]
        )
    )
