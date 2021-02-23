# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12941

def solution(A,B):
    return sum(a * b for a, b in zip(sorted(A), sorted(B, reverse=True)))