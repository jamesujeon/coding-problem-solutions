# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    def catch(x: int) -> int:
        for y in range(len(board)):
            if board[y][x - 1] > 0:
                doll = board[y][x - 1]
                board[y][x - 1] = 0
                return doll
        return 0

    answer = 0
    basket = []
    for move in moves:
        doll = catch(move)
        if doll == 0:
            continue

        if not basket or doll != basket[-1]:
            basket.append(doll)
        else:
            basket.pop()
            answer += 2

    return answer