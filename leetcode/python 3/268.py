# 문제 링크: https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (len(nums) * (len(nums) + 1)) // 2 - sum(nums)