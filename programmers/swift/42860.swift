// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42860

func solution(_ name: String) -> Int {
    let alphabets = Array("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    let code = name.compactMap { alphabets.firstIndex(of: $0) }

    var minMove = code.count - 1
    var i = 0
    while i < code.count / 2,
          let next = code[(i + 1)...].firstIndex(where: { $0 > 0 })
    {
        minMove = min(code.count + i * 2 - next, minMove)
        i = next
    }

    return code.reduce(0) { $0 + min($1, 26 - $1) } + minMove
}