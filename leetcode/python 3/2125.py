# 문제 링크: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        devices = [count for count in [row.count('1') for row in bank] if count > 0]

        return sum(devices[i] * devices[i - 1] for i in range(1, len(devices))) if len(devices) > 1 else 0
