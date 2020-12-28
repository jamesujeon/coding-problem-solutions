# 문제 링크: https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        pick_range = [1, n]
        while True:
            pick = sum(pick_range) // 2
            result = guess(pick)
            if result > 0:
                pick_range[0] = pick + 1
            elif result < 0:
                pick_range[1] = pick - 1
            else:
                return pick