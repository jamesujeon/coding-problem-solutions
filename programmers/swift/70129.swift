// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/70129

func solution(_ s: String) -> [Int] {
    var s = s
    var counts = [0, 0]

    while s != "1" {
        let nonzeros = s.filter { $0 == "1" }.count
        let zeros = s.count - nonzeros

        s = String(nonzeros, radix: 2)
        counts[0] += 1
        counts[1] += zeros
    }

    return counts
}