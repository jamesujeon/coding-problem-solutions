# 문제 링크: https://leetcode.com/problems/delete-characters-to-make-fancy-string/

class Solution:
    def makeFancyString(self, s: str) -> str:
        fancy_s = ''

        prev_i = 0
        for i in range(len(s)):
            if s[i] != s[prev_i]:
                prev_i = i

            if i - prev_i < 2:
                fancy_s += s[i]

        return fancy_s
