// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42862

func solution(_ n:Int, _ lost:[Int], _ reserve:[Int]) -> Int {
    let reserveLost = Set(lost).intersection(Set(reserve))
    var lost = Set(lost).subtracting(reserveLost).sorted()
    var reserve = Array(Set(reserve).subtracting(reserveLost))

    Array(lost).forEach { person in
        guard let index = lost.firstIndex(of: person) else { return }

        if let prevIndex = reserve.firstIndex(of: person - 1) {
            reserve.remove(at: prevIndex)
            lost.remove(at: index)
        } else if let nextIndex = reserve.firstIndex(of: person + 1) {
            reserve.remove(at: nextIndex)
            lost.remove(at: index)
        }
    }

    return n - lost.count
}