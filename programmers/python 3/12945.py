# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    F = [0, 1]
    for i in range(2, n + 1):
        F.append(F[i - 2] + F[i - 1])
    return F[n] % 1234567