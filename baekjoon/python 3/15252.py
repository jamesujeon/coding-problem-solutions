# 문제 링크: https://www.acmicpc.net/problem/15252

for x in range(1, int(input()) + 1):
    input()
    m = list(map(int, input().split()))
    for i in map(int, input().split()):
        m[i - 1] -= 1

    print(f"Data Set {x}:\n{max(m)}\n")
