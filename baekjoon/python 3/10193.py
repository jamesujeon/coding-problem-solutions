# 문제 링크: https://www.acmicpc.net/problem/10193

for _ in range(int(input())):
    w1, w2 = input().split()

    c = sum(ord(i) - ord(j) for i, j in zip(w1, w2))
    s = f"{'earned' if c > 0 else 'cost'} {abs(c)} coins" if c else "was FREE"
    print(f"Swapping letters to make {w1} look like {w2} {s}.")
