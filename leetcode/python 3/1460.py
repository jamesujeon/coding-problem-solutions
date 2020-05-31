# 문제 링크: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return collections.Counter(target) == collections.Counter(arr)
