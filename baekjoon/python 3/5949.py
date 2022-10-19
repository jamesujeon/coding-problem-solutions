# 문제 링크: https://www.acmicpc.net/problem/5949

N = input()

N = N[::-1]
N = ','.join(N[i:i + 3] for i in range(0, len(N), 3))
N = N[::-1]

print(N)
