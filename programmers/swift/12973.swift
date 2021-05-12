// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12973

func solution(_ s: String) -> Int {
    guard s.count % 2 == 0 else { return 0 }

    var stack = [Character]()
    for character in s {
        if let top = stack.last, top == character {
            stack.removeLast()
        } else {
            stack.append(character)
        }
    }

    return stack.isEmpty ? 1 : 0
}