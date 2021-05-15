// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12937

func solution(_ w: Int, _ h: Int) -> Int64 {
    Int64(w * h) - Int64(w + h - gcd(w, h))
}

func gcd(_ a: Int, _ b: Int) -> Int {
    var (a, b) = (a, b)
    while a % b != 0 {
        (a, b) = (b, a % b)
    }
    return b
}