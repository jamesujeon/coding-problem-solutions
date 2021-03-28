// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12910

func solution(_ arr:[Int], _ divisor:Int) -> [Int] {
    let result = arr.sorted().filter { $0 % divisor == 0 }
    return result.isEmpty ? [-1] : result
}