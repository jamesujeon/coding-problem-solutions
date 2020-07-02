# 문제 링크: https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

class Solution:
    def average(self, salary: List[int]) -> float:
        s = sorted(salary)[1:-1]
        return sum(s) / len(s)