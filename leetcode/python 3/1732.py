# 문제 링크: https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        for i in range(len(gain)):
            altitudes.append(altitudes[-1] + gain[i])

        return max(altitudes)