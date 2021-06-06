// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12932

func solution(_ n: Int64) -> [Int] {
    String(n)
        .compactMap { Int(String($0)) }
        .reversed()
}
