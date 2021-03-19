# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    lcm = n * m
    while n % m:
        n, m = m, n % m
    gcd = m
    lcm //= gcd
    return [gcd, lcm]