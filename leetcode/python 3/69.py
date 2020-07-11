# 문제 링크: https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        result, left, right = 0, 0, x // 2
        while left <= right:
            mid = (left + right) // 2
            if mid**2 > x:
                right = mid - 1
            else:
                result = mid
                left = mid + 1
        return result

    # def mySqrt(self, x: int) -> int:
    #     return int(math.sqrt(x))
