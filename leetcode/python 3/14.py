# 문제 링크: https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = ""
        for i in range(min(map(len, strs))):
            ch = strs[0][i]
            if all(s[i] == ch for s in strs):
                prefix += ch
            else:
                break
        return prefix