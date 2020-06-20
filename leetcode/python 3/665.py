# 문제 링크: https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # check if there is no more increasing element
                for j in range(i + 1, len(nums) - 1):
                    if nums[j] > nums[j + 1]:
                        return False
                # check if previous and next elements are non-decreasing
                return i == 0 or nums[i - 1] <= nums[i + 1] or i == len(nums) - 2 or nums[i] <= nums[i + 2]
        return True
