// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/17687

func solution(_ n: Int, _ t: Int, _ m: Int, _ p: Int) -> String {
    var s = [String]()
    var i = 0
    while s.count < t * m {
        s += String(i, radix: n).uppercased().map { String($0) }
        i += 1
    }

    return stride(from: p - 1, to: t * m, by: m)
        .map { s[$0] }
        .joined()
}
