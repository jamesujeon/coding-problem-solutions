// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12911

func solution(_ n:Int) -> Int {
    (n + 1 ... 1000000).first { $0.nonzeroBitCount == n.nonzeroBitCount } ?? n
}