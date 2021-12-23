# 문제 링크: https://leetcode.com/problems/sign-of-the-product-of-an-array/

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        return 0 if 0 in nums else (-1 if sum(num < 0 for num in nums) % 2 else 1)