# 문제 링크: https://leetcode.com/problems/largest-odd-number-in-string/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num) - 1
        while i > -1 and int(num[i]) % 2 == 0:
            i -= 1

        return num[:i + 1]