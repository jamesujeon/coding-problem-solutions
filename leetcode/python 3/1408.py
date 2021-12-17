# 문제 링크: https://leetcode.com/problems/string-matching-in-an-array/

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return [sub for sub in words if any(sub != word and sub in word for word in words)]