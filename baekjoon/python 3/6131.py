# 문제 링크: https://www.acmicpc.net/problem/6131

N = int(input())

print(sum(((B**2 + N)**.5).is_integer() for B in range(1, 501)))
