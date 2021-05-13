// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/60057

func solution(_ s: String) -> Int {
    (1...(s.count / 2 + 1)).map { compress(s, $0).count }.min()!
}

func compress(_ string: String, _ length: Int) -> String {
    let string = Array(string)
    var result = ""

    var i = 0
    while i < string.count {
        var count = 0
        let substring = string[i..<min(i + length, string.count)]
        while i < string.count && string[i..<min(i + length, string.count)] == substring {
            count += 1
            i += length
        }

        result += count > 1 ? "\(count)\(String(substring))" : String(substring)
    }

    return result
}