// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/70128

func solution(_ a: [Int], _ b: [Int]) -> Int {
    zip(a, b).map(*).reduce(0, +)
}