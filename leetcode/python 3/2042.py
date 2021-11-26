# 문제 링크: https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev_num = 0
        for s in s.split():
            if not s.isdecimal():
                continue

            if int(s) <= prev_num:
                return False

            prev_num = int(s)

        return True