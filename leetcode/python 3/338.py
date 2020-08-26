# 문제 링크: https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, num: int) -> List[int]:
        bins, dist = [0], 1
        for i in range(1, num + 1):
            if i == dist * 2:
                dist *= 2
            bins.append(bins[i - dist] + 1)
        return bins