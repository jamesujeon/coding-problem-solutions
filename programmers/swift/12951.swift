// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12951

import Foundation

extension StringProtocol {

    var capitalized: String {
        guard let first = first else { return "" }

        return first.uppercased() + dropFirst().lowercased()
    }
}

func solution(_ s: String) -> String {
    s.components(separatedBy: .whitespaces)
        .map { $0.capitalized }
        .joined(separator: " ")
}