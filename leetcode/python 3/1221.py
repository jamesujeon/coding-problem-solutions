# 문제 링크: https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        amount = 0
        balance = 0
        for c in s:
            balance += 1 if c == 'L' else -1
            if balance == 0:
                amount += 1
        return amount
