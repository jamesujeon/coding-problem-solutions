# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12905

def solution(board):
    if not max(board[0]) and not max(row[0] for row in board):
        return 0

    max_side = 1
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if not board[i][j]:
                continue
            board[i][j] = min(
                board[i - 1][j],
                board[i][j - 1],
                board[i - 1][j - 1]
            ) + 1
            max_side = max(board[i][j], max_side)

    return max_side**2