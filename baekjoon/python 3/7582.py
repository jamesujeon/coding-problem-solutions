# 문제 링크: https://www.acmicpc.net/problem/7582

while (s := input()) != '# 0':
    R, Z = s.split()
    P, Z = int(input()), int(Z)
    for _ in range(int(input())):
        p1, p2 = map(int, input().split())
        P = min(P - p1 + p2, Z)

    print(R, P)
