# 문제 링크: https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        return [i for i, num in enumerate(nums) if num == target]