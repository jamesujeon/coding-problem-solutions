# 문제 링크: https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            return True

        for _ in range(len(B) - 1):
            B = B[1:] + B[0]
            if A == B:
                return True
        return False