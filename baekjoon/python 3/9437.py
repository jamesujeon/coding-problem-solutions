# 문제 링크: https://www.acmicpc.net/problem/9437

while (s := input()) != '0':
    N, P = map(int, s.split())

    for i in range(N // 4):
        p = [i * 2 + 1, i * 2 + 2, N - i * 2 - 1, N - i * 2]
        if P in p:
            p.remove(P)
            print(*p)
            break
