# 문제 링크: https://leetcode.com/problems/special-positions-in-a-binary-matrix/

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        positions = 0
        for i in range(len(mat)):
            if sum(mat[i]) == 1:
                j = mat[i].index(1)
                if sum(mat[i][j] for i in range(len(mat))) == 1:
                    positions += 1
        return positions