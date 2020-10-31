# 문제 링크: https://leetcode.com/problems/binary-prefix-divisible-by-5/

class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        for i in range(1, len(A)):
            A[i] += A[i - 1] * 2
        return [n % 5 == 0 for n in A]
