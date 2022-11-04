# 문제 링크: https://www.acmicpc.net/problem/6975

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    divisors = set()
    for i in range(1, int(n**.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    divisors.remove(n)
    s = sum(divisors)

    result = 'a perfect'
    if n > s:
        result = 'a deficient'
    elif n < s:
        result = 'an abundant'

    print(f'{n} is {result} number.\n')
