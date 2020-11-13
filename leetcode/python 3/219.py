# 문제 링크: https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexes = {}
        for i in range(len(nums)):
            if nums[i] in indexes and i - indexes[nums[i]] <= k:
                return True
            indexes[nums[i]] = i
        return False