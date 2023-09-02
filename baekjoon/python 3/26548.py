# 문제 링크: https://www.acmicpc.net/problem/26548

for _ in range(int(input())):
    a, b, c = map(float, input().split())

    d = (b * b - 4 * a * c)**.5
    print(f"{(-1 * b + d) / (2 * a):.3f}, {(-1 * b - d) / (2 * a):.3f}")
