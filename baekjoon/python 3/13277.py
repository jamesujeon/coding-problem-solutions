# 문제 링크: https://www.acmicpc.net/problem/13277

from decimal import Decimal, getcontext
getcontext().prec = 10**6

a, b = map(Decimal, input().split())
print(a * b)
