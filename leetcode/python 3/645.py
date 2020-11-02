# 문제 링크: https://leetcode.com/problems/set-mismatch/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        set_sum = sum(set(nums))
        return [sum(nums) - set_sum, sum(range(1, len(nums) + 1)) - set_sum]