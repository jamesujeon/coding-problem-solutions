# 문제 링크: https://leetcode.com/problems/determine-color-of-a-chessboard-square/

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return 'abcdefgh'.index(coordinates[0]) % 2 != '12345678'.index(coordinates[1]) % 2