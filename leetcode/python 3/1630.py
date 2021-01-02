# 문제 링크: https://leetcode.com/problems/arithmetic-subarrays/

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def is_arithmetic(nums: List[int]) -> bool:
            nums.sort()
            diff = nums[1] - nums[0]
            for i in range(1, len(nums) - 1):
                if nums[i + 1] - nums[i] != diff:
                    return False
            return True

        return [is_arithmetic(nums[l[i]:r[i] + 1]) for i in range(len(l))]