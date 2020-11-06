# 문제 링크: https://leetcode.com/problems/rearrange-spaces-between-words/

class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces, words = text.count(' '), text.split()
        if len(words) > 1:
            space = ' ' * (spaces // (len(words) - 1))
            end_space = ' ' * (spaces % (len(words) - 1))
            return space.join(words) + end_space
        else:
            return words[0] + (' ' * spaces)