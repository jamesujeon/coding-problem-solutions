# 문제 링크: https://leetcode.com/problems/flipping-an-image/

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        A = map(lambda r: reversed(r), A)
        return map(lambda r: map(lambda x: x ^ 1, r), A)
