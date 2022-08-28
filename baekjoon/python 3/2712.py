# 문제 링크: https://www.acmicpc.net/problem/2712

units = {'kg': (2.2046, 'lb'), 'lb': (0.4536, 'kg'), 'l': (0.2642, 'g'), 'g': (3.7854, 'l')}

for _ in range(int(input())):
    v, u = input().split()

    unit = units[u]
    print(f"{float(v) * unit[0]:.4f} {unit[1]}")
