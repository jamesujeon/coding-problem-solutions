// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42578

func solution(_ clothes:[[String]]) -> Int {
    var cases = [String: Int]()
    clothes.forEach { cloth in
        cases[cloth[1], default: 1] += 1
    }

    return cases.values.reduce(1, *) - 1
}