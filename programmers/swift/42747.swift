// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42747

func solution(_ citations: [Int]) -> Int {
    citations
        .sorted(by: >)
        .enumerated()
        .first { $0 >= $1 }?
        .offset ?? citations.count
}