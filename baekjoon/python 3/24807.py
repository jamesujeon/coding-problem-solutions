# 문제 링크: https://www.acmicpc.net/problem/24807

b, d, c, l = map(int, input().split())

has_solution = False
for i in range(l // b + 1):
    for j in range((l - b * i) // d + 1):
        k = l - i * b - j * d
        if k % c == 0:
            print(i, j, k // c)
            has_solution = True

if not has_solution:
    print("impossible")
