# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    h = 3
    while True:
        w = (brown - 2 * h + 4) // 2
        if w * h == brown + yellow:
            return [w, h]
        h += 1