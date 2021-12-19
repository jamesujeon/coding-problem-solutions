# 문제 링크: https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(len(nums), 0, -1):
            if sum(num >= i for num in nums) == i:
                return i

        return -1