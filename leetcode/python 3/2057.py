# 문제 링크: https://leetcode.com/problems/smallest-index-with-equal-value/

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if i % 10 == num:
                return i

        return -1