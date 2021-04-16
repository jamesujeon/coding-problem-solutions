// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12945

func solution(_ n:Int) -> Int {
    var a = 0
    var b = 1
    for _ in 2...n {
        (a, b) = (b, (a + b) % 1234567)
    }
    return b
}