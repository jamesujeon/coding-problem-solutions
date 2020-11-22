# 문제 링크: https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return next((letter for letter in letters if target < letter), letters[0])