// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12905

func solution(_ board:[[Int]]) -> Int {
    guard board[0].max() == 1 || board.map({ $0[0] }).max() == 1 else {
        return 0
    }

    var board = board
    var maxSide = 1
    for i in 1 ..< board.count {
        for j in 1 ..< board[0].count {
            guard board[i][j] == 1 else { continue }

            board[i][j] = min(
                board[i - 1][j],
                board[i][j - 1],
                board[i - 1][j - 1]
            ) + 1

            if board[i][j] > maxSide {
                maxSide = board[i][j]
            }
        }
    }

    return maxSide * maxSide
}