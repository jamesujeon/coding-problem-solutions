// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12985

func solution(_ n: Int, _ a: Int, _ b: Int) -> Int {
    var (a, b) = (a, b)

    var round = 0
    while a != b {
        a = (a + 1) / 2
        b = (b + 1) / 2
        round += 1
    }

    return round
}