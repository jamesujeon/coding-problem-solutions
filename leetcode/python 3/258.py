# 문제 링크: https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        return num and (num % 9 or 9)