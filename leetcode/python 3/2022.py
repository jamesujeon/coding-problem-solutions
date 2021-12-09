# 문제 링크: https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        return [original[(n * r):(n * (r + 1))] for r in range(m)] if len(original) == m * n else []