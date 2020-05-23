# 문제 링크: https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        values = {'U': 1, 'D': -1, 'R': 1, 'L': -1}
        pos = [0, 0]
        for move in moves:
            if move in 'LR':
                pos[0] += values[move]
            else:
                pos[1] += values[move]
        return pos == [0, 0]
