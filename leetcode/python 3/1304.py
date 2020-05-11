# 문제 링크: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = [i for i in range(-(n // 2), n // 2 + 1)]
        if not n % 2:
            result.remove(0)
        return result