# 문제 링크: https://leetcode.com/problems/sum-of-unique-elements/

from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(k for k, v in Counter(nums).items() if v == 1)