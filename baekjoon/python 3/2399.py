# 문제 링크: https://www.acmicpc.net/problem/2399

n = int(input())
x = sorted(map(int, input().split()))

print(sum(x[i] * (i * 2 - n + 1) * 2 for i in range(n)))
