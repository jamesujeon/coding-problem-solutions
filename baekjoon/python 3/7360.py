# 문제 링크: https://www.acmicpc.net/problem/7360

while (n := int(input())) != 0:
    p = [0, 0]
    for a, b in zip(map(int, input().split()), map(int, input().split())):
        if abs(a - b) == 1:
            p[a > b] += (a + b) * (1 + (a + b == 3))
        elif a != b:
            p[a < b] += max(a, b)

    print(f"A has {p[0]} points. B has {p[1]} points.\n")
