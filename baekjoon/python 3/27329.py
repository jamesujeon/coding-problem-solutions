# 문제 링크: https://www.acmicpc.net/problem/27329

N, S = int(input()) // 2, input()
print(('No', 'Yes')[S[:N] == S[N:]])
