# 문제 링크: https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in nums1:
            try:
                x = next(num2 for num2 in nums2[nums2.index(num) + 1:] if num2 > num)
            except:
                x = -1
            result.append(x)
        return result