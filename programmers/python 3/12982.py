# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    d.sort()

    price = 0
    for i in range(len(d)):
        price += d[i]
        if price > budget:
            return i

    return len(d)