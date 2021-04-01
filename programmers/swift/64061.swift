// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/64061

import Foundation

func solution(_ board:[[Int]], _ moves:[Int]) -> Int {
    var count = 0
    var board = board
    var basket = [Int]()

    for x in moves {
        guard let y = board.firstIndex(where: { $0[x - 1] > 0 }) else {
            continue
        }

        let doll = board[y][x - 1]
        board[y][x - 1] = 0

        if doll == basket.last {
            basket.popLast()
            count += 2
        } else {
            basket.append(doll)
        }
    }

    return count
}