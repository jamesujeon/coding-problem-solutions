# 문제 링크: https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = collections.Counter(nums)
        return [num for num in nums if nums[num] == 1][0]