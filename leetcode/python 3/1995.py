# 문제 링크: https://leetcode.com/problems/count-special-quadruplets/

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count, sums = 0, {}
        for b in range(1, len(nums) - 2):
            for a in range(b):
                sums[nums[a] + nums[b]] = sums.get(nums[a] + nums[b], 0) + 1
            for d in range(b + 2, len(nums)):
                count += sums.get(nums[d] - nums[b + 1], 0)

        return count
