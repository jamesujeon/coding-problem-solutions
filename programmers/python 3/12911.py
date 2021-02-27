# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    ones = bin(n).count('1')
    for i in range(n + 1, 1000001):
        if bin(i).count('1') == ones:
            return i