# 문제 링크: https://www.acmicpc.net/problem/10984

for _ in range(int(input())):
    credits = points = 0
    for _ in range(int(input())):
        C, G = map(float, input().split())
        credits += C
        points += C * G

    print(f"{int(credits)} {points / credits:.1f}")
