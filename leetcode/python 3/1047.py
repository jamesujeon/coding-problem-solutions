# 문제 링크: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

import re

class Solution:
    def removeDuplicates(self, S: str) -> str:
        regex = re.compile(r'([a-z])\1')
        while regex.search(S):
            S = regex.sub('', S)
        return S