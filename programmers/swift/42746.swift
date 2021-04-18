// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42746

func solution(_ numbers:[Int]) -> String {
    let numbers = numbers.map { String($0) }
        .sorted { Int($0 + $1)! > Int($1 + $0)! }

    return numbers[0] != "0" ? numbers.joined() : "0"
}