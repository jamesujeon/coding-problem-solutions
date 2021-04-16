// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42587

func solution(_ priorities:[Int], _ location:Int) -> Int {
    var priorities = priorities.enumerated().map { $0 }
    var count = 0

    while !priorities.isEmpty {
        let J = priorities.removeFirst()
        if priorities.contains(where: { $0.element > J.element }) {
            priorities.append(J)
        } else {
            count += 1
            if J.offset == location {
                break
            }
        }
    }

    return count
}