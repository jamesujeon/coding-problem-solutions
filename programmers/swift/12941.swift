// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12941

func solution(_ A: [Int], _ B: [Int]) -> Int {
    zip(A.sorted(), B.sorted { $0 > $1 }).map(*).reduce(0, +)
}