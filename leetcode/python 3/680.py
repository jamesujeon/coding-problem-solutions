# 문제 링크: https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        if is_palindrome(s):
            return True

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return is_palindrome(s[i:j]) or is_palindrome(s[i + 1:j + 1])
            i += 1
            j -= 1
        return False