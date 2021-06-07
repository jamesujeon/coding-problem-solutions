// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/76501

func solution(_ absolutes: [Int], _ signs: [Bool]) -> Int {
    zip(absolutes, signs).reduce(0) { $0 + ($1.1 ? $1.0 : -$1.0) }
}