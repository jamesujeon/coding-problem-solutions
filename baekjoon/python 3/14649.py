# 문제 링크: https://www.acmicpc.net/problem/14649

P = int(input())
s = [0] * 100
for _ in range(int(input())):
    n, d = input().split()
    r = range(int(n) - 1) if d == 'L' else range(int(n), 100)
    for i in r:
        s[i] = (s[i] + 1) % 3

for i in range(3):
    print(f"{P * s.count(i) / 100:.2f}")
