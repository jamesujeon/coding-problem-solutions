# 문제 링크: https://leetcode.com/problems/largest-number-at-least-twice-of-others/

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        return (nums.index(max(nums)) if max(nums) >= sorted(nums)[-2] * 2 else -1) if len(nums) > 1 else 0
