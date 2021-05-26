# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    return (int(n ** .5) + 1) ** 2 if int(n ** .5) ** 2 == n else -1