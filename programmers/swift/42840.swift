// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42840

import Foundation

func solution(_ answers:[Int]) -> [Int] {
    let patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    ]

    let scores = patterns
        .enumerated()
        .map { i, pattern in
            answers
                .enumerated()
                .map { j, answer in
                    pattern[j % pattern.count] == answer ? 1 : 0
                }
                .reduce(0, +)
        }
    let maxScore = scores.max()

    return scores
        .enumerated()
        .compactMap { i, score in
            score == maxScore ? i + 1 : nil
        }
}