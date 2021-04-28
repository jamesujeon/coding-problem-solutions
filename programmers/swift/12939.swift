// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12939

func solution(_ s: String) -> String {
    let numbers = s.split(separator: " ").compactMap { Int($0) }
    return "\(numbers.min()!) \(numbers.max()!)"
}