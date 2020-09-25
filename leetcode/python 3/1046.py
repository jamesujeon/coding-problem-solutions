# 문제 링크: https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            stone = stones.pop() - stones.pop()
            if stone:
                stones.append(stone)
        return stones[0] if stones else 0