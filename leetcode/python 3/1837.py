# 문제 링크: https://leetcode.com/problems/sum-of-digits-in-base-k/

class Solution:
    def sumBase(self, n: int, k: int) -> int:
        result = 0
        while n:
            result += n % k
            n //= k

        return result