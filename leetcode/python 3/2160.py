# 문제 링크: https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

class Solution:
    def minimumSum(self, num: int) -> int:
        digits = sorted(str(num))

        return int(digits[0] + digits[2]) + int(digits[1] + digits[3])
