// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12922

func solution(_ n:Int) -> String {
    return String(repeating: "수박", count: n / 2) + (n % 2 == 0 ? "" : "수")
}