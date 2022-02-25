# 문제 링크: https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

class Solution:
    removed = False

    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                if self.removed:
                    return False
                self.removed = True

                return (
                    self.canBeIncreasing(nums[i - 2:i - 1] + nums[i:]) or 
                    self.canBeIncreasing(nums[i - 1:i] + nums[i + 1:])
                )

        return True
