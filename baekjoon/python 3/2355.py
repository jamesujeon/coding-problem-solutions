# 문제 링크: https://www.acmicpc.net/problem/2355

A, B = sorted(map(int, input().split()))

print((A + B) * (B - A + 1) // 2)
