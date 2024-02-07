# 문제 링크: https://www.acmicpc.net/problem/4636

while (n := int(input())) != -1:
    s = []
    for _ in range(n):
        a, b, c, d = input().split()
        s.append((int(a) * int(b) * int(c), d))
    s.sort()

    print(f'{s[-1][1]} took clay from {s[0][1]}.')
