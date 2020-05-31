# 문제 링크: https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = [nums.pop()]
        while sum(result) <= sum(nums):
            result.append(nums.pop())
        return result
