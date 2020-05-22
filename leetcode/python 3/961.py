# 문제 링크: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for i in A:
            if A.count(i) > 1:
                return i
