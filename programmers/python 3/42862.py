# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    reserve_lost = set(lost).intersection(set(reserve))
    lost = sorted(set(lost) - reserve_lost)
    reserve = list(set(reserve) - reserve_lost)

    lost_count = 0
    for p in lost:
        if p + 1 in reserve:
            reserve.remove(p + 1)
        elif p - 1 not in reserve:
            lost_count += 1
    return n - lost_count