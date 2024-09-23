# 문제 링크: https://www.acmicpc.net/problem/11922

N, B = input().split()
C = {'A': (11, 11), 'K': (4, 4), 'Q': (3, 3), 'J': (20, 2), 'T': (10, 10), '9': (14, 0), '8': (0, 0), '7': (0, 0)}
P = 0
for _ in range(int(N) * 4):
    K = input()
    P += C[K[0]][K[1] != B]

print(P)
