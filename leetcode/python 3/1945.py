# 문제 링크: https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = ''.join(str(ord(ch) - 96) for ch in s)
        for _ in range(k):
            s = sum(map(int, str(s)))

        return s