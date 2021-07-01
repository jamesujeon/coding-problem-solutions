# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    return sum(-i if int(i ** .5) ** 2 == i else i for i in range(left, right + 1))