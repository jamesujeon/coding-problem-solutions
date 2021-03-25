// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12912

func solution(_ a:Int, _ b:Int) -> Int64 {
    let n1 = Int64(min(a, b))
    let n2 = Int64(max(a, b))

    return ((n2 * (n2 + 1)) - (n1 * (n1 - 1))) / 2
}