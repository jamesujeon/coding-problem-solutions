# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answers = [words[0]]
    for word in words[1:]:
        if word[0] != answers[-1][-1] or word in answers:
            return [len(answers) % n + 1, len(answers) // n + 1]

        answers.append(word)

    return [0, 0]