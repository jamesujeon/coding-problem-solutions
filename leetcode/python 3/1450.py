# 문제 링크: https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(startTime[i] <= queryTime and queryTime <= endTime[i] for i in range(len(startTime)))
