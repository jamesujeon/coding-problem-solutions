// 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12981

func solution(_ n: Int, _ words: [String]) -> [Int] {
    var answers = [words[0]]
    for word in words.dropFirst() {
        guard word.first == answers.last!.last, !answers.contains(word) else {
            return [answers.count % n + 1, answers.count / n + 1]
        }

        answers.append(word)
    }

    return [0, 0]
}