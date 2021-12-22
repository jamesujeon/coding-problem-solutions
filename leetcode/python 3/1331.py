# 문제 링크: https://leetcode.com/problems/rank-transform-of-an-array/

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {num: i + 1 for i, num in enumerate(sorted(set(arr)))}

        return [rank[num] for num in arr]