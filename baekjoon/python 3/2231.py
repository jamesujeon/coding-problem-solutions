# 문제 링크: https://www.acmicpc.net/problem/2231

N = int(input())


for M in range(max(N - len(str(N)) * 9, 1), N + 1):
    if M + sum(map(int, str(M))) == N:
        print(M)
        break
else:
    print(0)