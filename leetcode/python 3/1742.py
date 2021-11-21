# 문제 링크: https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        numbers = {}
        for n in range(lowLimit, highLimit + 1):
            n = sum(map(int, str(n)))
            if n not in numbers:
                numbers[n] = 0
            numbers[n] += 1

        return max(numbers.values())
