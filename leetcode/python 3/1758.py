# 문제 링크: https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

class Solution:
    def minOperations(self, s: str) -> int:
        changes = sum(ch != ('1' if i % 2 else '0') for i, ch in enumerate(s))

        return min(changes, len(s) - changes)