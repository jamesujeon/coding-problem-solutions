# 문제 링크: https://leetcode.com/problems/intersection-of-two-arrays-ii/

from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return sum([[k] * v for k, v in (Counter(nums1) & Counter(nums2)).items()], [])
