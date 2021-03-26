// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42748

import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    return commands.map { command in
        array[command[0] - 1 ..< command[1]].sorted()[command[2] - 1]
    }
}