# 문제 링크: https://leetcode.com/problems/three-divisors/

class Solution:
    def isThree(self, n: int) -> bool:
        return sum(n % i == 0 for i in range(1, n + 1)) == 3