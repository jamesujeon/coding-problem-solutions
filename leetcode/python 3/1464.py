# 문제 링크: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_num = max(nums)
        nums.remove(max_num)
        return (max_num - 1) * (max(nums) - 1)
