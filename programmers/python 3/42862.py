# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    reserve_lost = set(lost).intersection(set(reserve))
    lost = sorted(set(lost) - reserve_lost)
    reserve = list(set(reserve) - reserve_lost)

    for p in list(lost):
        if p - 1 in reserve:
            reserve.remove(p - 1)
            lost.remove(p)
        elif p + 1 in reserve:
            reserve.remove(p + 1)
            lost.remove(p)
    return n - len(lost)