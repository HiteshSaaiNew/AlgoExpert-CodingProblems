from collections import defaultdict
from collections import deque


class Solution:
    def topologicalSort(self, jobs, deps):
        ## Time O(j+p) || Space O(j+p)

        preReqs = defaultdict(list)
        jobGraph = defaultdict(list)

        for dep in deps:
            prereq, course = dep
            preReqs[prereq].append(course)

        for dep in deps:
            prereq, course = dep
            jobGraph[course].append(prereq)

        currJobs = deque([])
        for job in jobs:
            if job not in jobGraph:
                currJobs.append(job)

        if not currJobs:
            return []

        jobOrder = []
        while currJobs:

            job = currJobs.popleft()
            jobOrder.append(job)

            dependedJobs = preReqs[job]
            for depended in dependedJobs:
                jobGraph[depended].remove(job)
                if jobGraph[depended] == []:
                    currJobs.append(depended)
                    del jobGraph[depended]

        if not jobGraph:
            return jobOrder

        return []


if __name__ == "__main__":

    print(
        Solution().topologicalSort(
            [1, 2, 3, 4], [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
        )
    )

    print(
        Solution().topologicalSort(
            [1, 2, 3, 4, 5, 6, 7, 8],
            [
                [1, 2],
                [1, 3],
                [1, 4],
                [1, 5],
                [1, 6],
                [1, 7],
                [2, 8],
                [3, 8],
                [4, 8],
                [5, 8],
                [6, 8],
                [7, 8],
            ],
        )
    )
