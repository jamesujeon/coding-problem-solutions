# 문제 링크: https://www.acmicpc.net/problem/11800

import sys
input = sys.stdin.readline

names = [
    ["Yakk", "Doh", "Seh", "Ghar", "Bang", "Sheesh"],
    ["Habb Yakk", "Dobara", "Dousa", "Dorgy", "Dabash", "Dosh"]
]

for n in range(1, int(input()) + 1):
    a, b = sorted(map(int, input().split()), reverse=True)

    result = names[0][a - 1] + ' ' + names[0][b - 1]
    if a == b:
        result = names[1][a - 1]
    elif a == 6 and b == 5:
        result = "Sheesh Beesh"

    print(f"Case {n}: {result}")
