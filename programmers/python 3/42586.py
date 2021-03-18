# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42586

from math import ceil

def solution(progresses, speeds):
    answer, current_day = [], 0
    for day in [ceil((100 - p) / s) for p, s in zip(progresses, speeds)]:
        if day > current_day:
            current_day = day
            answer.append(1)
        else:
            answer[-1] += 1
    return answer