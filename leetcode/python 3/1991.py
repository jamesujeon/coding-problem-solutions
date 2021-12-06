# 문제 링크: https://leetcode.com/problems/find-the-middle-index-in-array/

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        l, r = 0, sum(nums)
        for i in range(len(nums)):
            r -= nums[i]
            if l == r:
                return i
            l += nums[i]

        return -1