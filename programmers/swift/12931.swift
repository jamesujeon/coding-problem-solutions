// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12931

func solution(_ n: Int) -> Int {
    String(n)
        .compactMap { Int(String($0)) }
        .reduce(0, +)
}
