# 문제 링크: https://leetcode.com/problems/reformat-the-string/

class Solution:
    def reformat(self, s: str) -> str:
        s1 = s2 = ''
        for ch in s:
            if ch.isalpha():
                s1 += ch
            else:
                s2 += ch
        diff = abs(len(s1) - len(s2))
        if diff > 1:
            return ''

        result = ''
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        for i in range(len(s1)):
            result += s2[i] + s1[i]
        if diff:
            result += s2[-1]
        return result