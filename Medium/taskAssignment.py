class Solution:
    def taskAssignment(self, tasks, k):
        # Time O(nlog(n)) || Space O(n)
        if len(tasks) != k * 2:
            return []

        res = []
        taskDurationIdx = self.getTaskIdx(tasks)
        tasks.sort()
        for i in range(k):

            taskTime1 = tasks[i]
            allIdxTask1 = taskDurationIdx[taskTime1]
            currIdxTask1 = allIdxTask1.pop()

            idx2 = len(tasks) - 1 - i
            taskTime2 = tasks[idx2]
            allIdxTask2 = taskDurationIdx[taskTime2]
            currIdxTask2 = allIdxTask2.pop()

            res.append([currIdxTask1, currIdxTask2])

        return res

    def getTaskIdx(self, tasks):
        taskAndIdx = {}
        for idx, task in enumerate(tasks):

            if task not in taskAndIdx:
                taskAndIdx[task] = [idx]
            else:
                taskAndIdx[task].append(idx)

        return taskAndIdx


if __name__ == "__main__":

    print(Solution().taskAssignment([1, 3, 5, 3, 1, 4], 3))
    print(Solution().taskAssignment([1, 8, 9, 10], 2))
    print(Solution().taskAssignment([2, 1, 3, 4, 5, 13, 12, 9, 11, 10, 6, 7, 14, 8], 7))
