// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/77484

func solution(_ lottos: [Int], _ winNums: [Int]) -> [Int] {
    let minWins = Set(winNums).intersection(lottos).count
    let maxWins = lottos.filter { $0 == 0 }.count + minWins
    return [min(7 - maxWins, 6), min(7 - minWins, 6)]
}