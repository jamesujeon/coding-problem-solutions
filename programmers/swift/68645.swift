// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/68645

func solution(_ n:Int) -> [Int] {
    var numbers = Array((1...n).map { [Int](repeating: 0, count: $0) })
    var (i, j, number) = (-1, 0, 1)

    for step in (0..<n) {
        for _ in (step..<n) {
            if step % 3 == 0 {
                i += 1
            } else if step % 3 == 1 {
                j += 1
            } else {
                i -= 1
                j -= 1
            }

            numbers[i][j] = number
            number += 1
        }
    }

    return numbers.flatMap { $0 }
}