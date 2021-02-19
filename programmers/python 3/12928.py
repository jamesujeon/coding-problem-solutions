# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12928

def solution(n):
    return sum(
        i + n // i if i != n // i else i
        for i in range(1, int(n**.5) + 1) 
        if n % i == 0
    )