# 문제 링크: https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        points = []
        point = 0
        for op in ops:
            if op != "C":
                if op == "+":
                    points.append(points[-1] + points[-2])
                elif op == "D":
                    points.append(points[-1] * 2)
                else:
                    points.append(int(op))
                point += points[-1]
            else:
                point -= points.pop()
        return point