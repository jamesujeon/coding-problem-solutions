# 문제 링크: https://www.acmicpc.net/problem/8320

n = int(input())
print(sum(n // i - i + 1 for i in range(1, int(n**.5) + 1)))
