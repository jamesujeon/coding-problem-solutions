# 문제 링크: https://www.acmicpc.net/problem/1731

n = [int(input()) for _ in range(int(input()))]

if n[0] + n[2] == n[1] * 2:
    print(n[-1] + (n[1] - n[0]))
else:
    print(n[-1] * (n[1] // n[0]))
