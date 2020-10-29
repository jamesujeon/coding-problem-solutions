# 문제 링크: https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        power = 1
        while power < num:
            power *= 4
        return power == num if num != 1 else True