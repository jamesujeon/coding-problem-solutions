# 문제 링크: https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        chips = collections.Counter(chip % 2 for chip in position)
        return min(chips[0], chips[1]) if len(chips) > 1 else 0