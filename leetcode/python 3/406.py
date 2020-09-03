# 문제 링크: https://leetcode.com/problems/queue-reconstruction-by-height/

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = []
        for p in sorted(people, key=lambda p: (p[0], -p[1]), reverse=True):
            result.insert(p[1], p)
        return result