# 문제 링크: https://www.acmicpc.net/problem/10185

for _ in range(int(input())):
    p, q = map(int, input().split())
    f = p * q / (p + q)

    print(f"f = {f:.1f}")
