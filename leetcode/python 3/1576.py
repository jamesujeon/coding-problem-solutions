# 문제 링크: https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

class Solution:
    def modifyString(self, s: str) -> str:
        for i in range(len(s)):
            if s[i] == '?':
                for ch in 'abc':
                    if ch * 2 not in s[:i] + ch + s[i + 1:]:
                        s = s[:i] + ch + s[i + 1:]
                        break

        return s
