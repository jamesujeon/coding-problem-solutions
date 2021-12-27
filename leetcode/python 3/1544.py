# 문제 링크: https://leetcode.com/problems/make-the-string-great/

class Solution:
    def makeGood(self, s: str) -> str:
        converted = []
        for i in range(len(s)):
            if converted and abs(ord(s[i]) - ord(converted[-1])) == 32:
                converted.pop()
            else:
                converted.append(s[i])

        return ''.join(converted)