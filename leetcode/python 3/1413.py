# 문제 링크: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sums = [-1]
        for num in nums:
            sums.append(sums[-1] + num)
        return max(-min(sums), 1)