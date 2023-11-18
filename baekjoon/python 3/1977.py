# 문제 링크: https://www.acmicpc.net/problem/1977

M, N = int(input()), int(input())

n = [i * i for i in range(int(M**.5) + int(int(M**.5)**2 != M), int(N**.5) + 1)]

if n:
    print(sum(n))
    print(n[0])
else:
    print(-1)
