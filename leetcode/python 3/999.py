# 문제 링크: https://leetcode.com/problems/available-captures-for-rook/

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        R = next((i, j) for i in range(8) for j in range(8) if board[i][j] == 'R')
        count = 0
        count += next((board[i][R[1]] == 'p' for i in range(R[0] - 1, -1, -1) if board[i][R[1]] != '.'), 0)
        count += next((board[R[0]][j] == 'p' for j in range(R[1] - 1, -1, -1) if board[R[0]][j] != '.'), 0)
        count += next((board[i][R[1]] == 'p' for i in range(R[0] + 1, 8) if board[i][R[1]] != '.'), 0)
        count += next((board[R[0]][j] == 'p' for j in range(R[1] + 1, 8) if board[R[0]][j] != '.'), 0)
        return count
