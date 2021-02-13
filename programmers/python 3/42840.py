# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    marks = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    scores = [0] * 3
    for i in range(len(answers)):
        for j in range(3):
            scores[j] += answers[i] == marks[j][i % len(marks[j])]
    max_score = max(scores)
    return sorted(i + 1 for i in range(3) if scores[i] == max_score)