// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12954

func solution(_ x: Int, _ n: Int) -> [Int64] {
    (1...n).map { Int64($0 * x) }
}