# 문제 링크: https://www.acmicpc.net/problem/25270

N = int(input())

if N < 100:
    print(99)
else:
    N1 = int(str(N // 100) + "99")
    N2 = N1 - 100
    print(N1 if N1 - N <= N - N2 else N2)
