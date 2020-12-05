# 문제 링크: https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return all(ransomNote.count(ch) <= magazine.count(ch) for ch in set(ransomNote))