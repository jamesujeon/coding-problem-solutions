# 문제 링크: https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def convert(s: str) -> str:
            stack = []
            for ch in s:
                if ch != '#':
                    stack.append(ch)
                elif stack:
                    stack.pop()
            return ''.join(stack)

        return convert(S) == convert(T)