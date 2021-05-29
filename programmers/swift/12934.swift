// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12934

import Foundation

func solution(_ n: Int64) -> Int64 {
    Int64(pow(floor(sqrt(Double(n))), 2)) == n ? Int64(pow(sqrt(Double(n)) + 1, 2)) : -1
}
