# 문제 링크: https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judges = list(set(range(1, n + 1)) - set(a for a, _ in trust))
        trusted = [b for _, b in trust]

        return judges[0] if len(judges) == 1 and trusted.count(judges[0]) == n - 1 else -1
