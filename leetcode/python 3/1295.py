# 문제 링크: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(not len(str(n)) % 2 for n in nums)
