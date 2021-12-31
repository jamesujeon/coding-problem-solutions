# 문제 링크: https://leetcode.com/problems/minimum-distance-to-the-target-element/

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        for distance in range(max(start, len(nums) - start - 1) + 1):
            l, r = start - distance, start + distance
            if (l >= 0 and nums[l] == target) or (r < len(nums) and nums[r] == target):
                return distance

        return 0