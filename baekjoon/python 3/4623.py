# 문제 링크: https://www.acmicpc.net/problem/4623

while (s := input()) != '0 0 0 0':
    A, B, C, D = map(int, s.split())

    if A > B: A, B = B, A
    if C > D: C, D = D, C

    print(f'{min(C * 100 // A, D * 100 // B, 100)}%')
