// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12930

func solution(_ s:String) -> String {
    return s
        .components(separatedBy: " ")
        .map { $0
            .enumerated()
            .map { $0 % 2 == 0 ? $1.uppercased() : $1.lowercased() }
            .joined()
        }
        .joined(separator: " ")
}