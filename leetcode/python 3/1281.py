# 문제 링크: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

from functools import reduce

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return reduce(lambda x, y: x * int(y), str(n), 1) - reduce(lambda x, y: x + int(y), str(n), 0)
