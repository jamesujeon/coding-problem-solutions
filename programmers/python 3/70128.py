# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    return sum(a * b for a, b in zip(a, b))