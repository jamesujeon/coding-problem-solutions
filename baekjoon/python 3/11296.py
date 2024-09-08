# 문제 링크: https://www.acmicpc.net/problem/11296

ds = {'R': 0.55, 'G': 0.7, 'B': 0.8, 'Y': 0.85, 'O': 0.9, 'W': 0.95}

for _ in range(int(input())):
    p, d, cp, c = input().split()

    p = float(p) * ds[d] * (0.95 if cp == 'C' else 1)
    if c == 'C':
        p *= 100
        p = (p + (10 if p % 10 > 5 else 0)) // 10 / 10

    print(f"${p:.2f}")
