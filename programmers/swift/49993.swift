// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/49993

func solution(_ skill: String, _ skillTrees: [String]) -> Int {
    skillTrees
        .map { skill.starts(with: $0.filter { skill.contains($0) }) ? 1 : 0 }
        .reduce(0, +)
}