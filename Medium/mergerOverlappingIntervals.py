class Solution:
    def mergeOverlappingIntervals(self, intervals):
        ## Time O(nlogn) || Space O(1)
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda interval: interval[0])
        left = 0
        right = 1
        while right < len(intervals):
            start1, end1 = intervals[left]
            start2, end2 = intervals[right]
            if start2 > start1 and start2 > end1:
                left += 1
                right += 1
            else:
                mergeStart = min(start1, start2)
                mergeEnd = max(end1, end2)
                intervals[left] = [mergeStart, mergeEnd]
                del intervals[right]

        return intervals


if __name__ == "__main__":

    print(
        Solution().mergeOverlappingIntervals([[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]])
    )
    print(
        Solution().mergeOverlappingIntervals(
            [
                [1, 10],
                [10, 20],
                [20, 30],
                [30, 40],
                [40, 50],
                [50, 60],
                [60, 70],
                [70, 80],
                [80, 90],
                [90, 100],
            ]
        )
    )
