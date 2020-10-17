# 문제 링크: https://leetcode.com/problems/base-7/

class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num:
            return str(num)

        sign = '-' if num < 0 else ''
        num = abs(num)
        result = []
        while num:
            result.append(str(num % 7))
            num //= 7
        result.append(sign)
        return ''.join(reversed(result))
