# 문제 링크: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums = list(zip(nums, sorted(nums)))
        num_range = range(len(nums))
        start_idx = next((i for i in num_range if nums[i][0] != nums[i][1]), 0)
        end_idx = next((i for i in reversed(num_range) if nums[i][0] != nums[i][1]), 0)
        return end_idx - start_idx + 1 if start_idx or end_idx else 0