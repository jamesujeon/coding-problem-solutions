# 문제 링크: https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            for ch in word:
                if ch not in allowed:
                    count += 1
                    break
        return len(words) - count