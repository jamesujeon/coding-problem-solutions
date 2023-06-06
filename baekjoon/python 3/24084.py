# 문제 링크: https://www.acmicpc.net/problem/24084

N, S = int(input()), input()

for i in range(1, N):
    if S[i] == 'J':
        print(S[i - 1])
