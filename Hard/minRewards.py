class Solution:
    def minRewards(self, scores):
        # Time O(n) || Space O(n)
        rewards = [1] * len(scores)

        for i in range(1, len(scores)):

            if scores[i] > scores[i - 1]:
                rewards[i] = rewards[i - 1] + 1

        for j in reversed(range(len(scores) - 1)):

            if scores[j] > scores[j + 1]:
                rewards[j] = max(rewards[j], rewards[j + 1] + 1)

        return sum(rewards)


if __name__ == "__main__":

    print(Solution().minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]))
    print(Solution().minRewards([2, 1, 4, 3, 6, 5, 8, 7, 10, 9]))