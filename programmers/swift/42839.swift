// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42839

import Foundation

func combinations(_ characters: [Character]) -> Set<Int> {
    guard !characters.isEmpty else { return [] }

    return Set(
        (0..<characters.count)
            .flatMap { i -> [String] in
                var characters = characters
                let elem = String(characters.remove(at: i))
                return [elem] + combinations(characters).map { String($0) + elem }
            }
            .compactMap { Int($0) }
    )
}

func isPrime(_ number: Int) -> Bool {
    guard number > 1 else { return false }

    for i in 2..<(Int(sqrt(Double(number))) + 1) {
        if number % i == 0 {
            return false
        }
    }
    return true
}

func solution(_ numbers: String) -> Int {
    return combinations(Array(numbers)).filter(isPrime).count
}