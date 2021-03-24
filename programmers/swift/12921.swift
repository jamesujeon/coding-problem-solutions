// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12921

import Foundation

func solution(_ n: Int) -> Int {
    var primes = [Bool](repeating: true, count: n + 1)
    primes[..<2] = [false, false]

    for i in 2..<(Int(sqrt(Double(n))) + 1) {
        if !primes[i] { continue }

        for j in stride(from: Int(pow(Double(i), 2)), to: n + 1, by: i) {
            primes[j] = false
        }
    }

    return primes
        .filter { $0 }
        .count
}