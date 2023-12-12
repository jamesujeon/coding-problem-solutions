# 문제 링크: https://www.acmicpc.net/problem/2756

import sys
input = sys.stdin.readline

def s(p):
    score = 0
    for p in (p[:2], p[2:4], p[4:]):
        d = (p[0]**2 + p[1]**2)**.5
        if d <= 3: score += 100
        elif d <= 6: score += 80
        elif d <= 9: score += 60
        elif d <= 12: score += 40
        elif d <= 15: score += 20
    return score

for _ in range(int(input())):
    p = list(map(float, input().split()))
    s1, s2 = s(p[:6]), s(p[6:])

    result = "TIE"
    if s1 != s2:
        result = f"PLAYER {1 if s1 > s2 else 2} WINS"

    print(f"SCORE: {s1} to {s2}, {result}.")
