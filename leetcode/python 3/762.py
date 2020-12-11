# 문제 링크: https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        return sum(bin(i).count('1') in primes for i in range(L, R + 1))