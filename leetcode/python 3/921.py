# 문제 링크: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        counts = {'(': 0, ')': 0}
        for p in S:
            if p == ')' and counts['(']:
                counts['('] -= 1
            else:
                counts[p] += 1
        return sum(counts.values())