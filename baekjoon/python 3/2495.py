# 문제 링크: https://www.acmicpc.net/problem/2495

for _ in range(3):
    n = input()

    max_c = c = 1
    for i in range(len(n) - 1):
        if n[i] == n[i + 1]:
            c += 1
        else:
            max_c = max(c, max_c)
            c = 1

    print(max(c, max_c))
