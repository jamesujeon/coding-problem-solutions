# 문제 링크: https://www.acmicpc.net/problem/27251

for k in range(1, int(input()) + 1):
    s = '*' * min(k * k, 100)
    if k > 10:
        s += "..."

    print(s)
