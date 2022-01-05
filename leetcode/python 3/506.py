# 문제 링크: https://leetcode.com/problems/relative-ranks/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        ranks = {s: str(i + 1) if i > 2 else medals[i] for i, s in enumerate(sorted(score, reverse=True))}

        return [ranks[s] for s in score]