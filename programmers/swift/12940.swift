// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12940

func solution(_ n:Int, _ m:Int) -> [Int] {
    var n = n
    var m = m

    var lcm = n * m
    while n % m != 0 {
        let temp = n
        n = m
        m = temp % m
    }
    let gcd = m
    lcm /= gcd

    return [gcd, lcm]
}