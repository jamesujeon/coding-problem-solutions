# 문제 링크: https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n // 2 + 1):
            complement = n - i
            if '0' not in f'{i}{n - i}':
                return [i, complement]