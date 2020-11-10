# 문제 링크: https://leetcode.com/problems/perfect-number/

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        total = 1 + sum(i + num // i for i in range(2, int(num**0.5) + 1) if num % i == 0)
        return num > 1 and num == total