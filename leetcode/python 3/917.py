# 문제 링크: https://leetcode.com/problems/reverse-only-letters/

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        i, j = 0, len(S) - 1
        while i < j:
            if S[i].isalpha() and S[j].isalpha():
                S[i], S[j] = S[j], S[i]
            elif S[i].isalpha():
                i -= 1
            elif S[j].isalpha():
                j += 1
            i += 1
            j -= 1
        return ''.join(S)