// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42586

import Foundation

func solution(_ progresses: [Int], _ speeds: [Int]) -> [Int] {
    var functions = [Int]()
    var currentDay = 0

    zip(progresses, speeds)
        .map { Int(ceil(Double(100 - $0) / Double($1))) }
        .forEach { day in
            if day > currentDay {
                currentDay = day
                functions.append(1)
            } else {
                functions[functions.count - 1] += 1
            }
        }

    return functions
}