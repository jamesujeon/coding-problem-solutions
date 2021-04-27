// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12953

func gcd(_ a: Int, _ b: Int) -> Int {
    var (a, b) = (a, b)
    while a % b != 0 {
        (a, b) = (b, a % b)
    }
    return b
}

func solution(_ arr: [Int]) -> Int {
    arr[1...].reduce(arr[0]) { result, number in
        result * (number / gcd(result, number))
    }
}