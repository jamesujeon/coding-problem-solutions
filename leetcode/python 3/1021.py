# 문제 링크: https://leetcode.com/problems/remove-outermost-parentheses/

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = ''
        valance = 0
        for c in S:
            if c == '(':
                valance += 1
                if valance == 1:
                    continue
            else:
                valance -= 1
                if valance == 0:
                    continue
            result += c

        return result
