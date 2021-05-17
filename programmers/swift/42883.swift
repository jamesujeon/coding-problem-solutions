// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42883

func solution(_ number: String, _ k: Int) -> String {
    let number = number.map(String.init)
    let resultCount = number.count - k
    var k = k

    var result = [String]()
    for i in 0..<number.count {
        while let last = result.last, last < number[i], k > 0 {
            result.popLast()
            k -= 1
        }
        result.append(number[i])
    }

    return result[..<resultCount].joined()
}