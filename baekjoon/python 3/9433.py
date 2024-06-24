# 문제 링크: https://www.acmicpc.net/problem/9433

for _ in range(int(input())):
    v = list(map(int, input().split()))

    for i in range(19)[::-1]:
        v[i] += v[i + 1] // 2
        v[i + 1] %= 2

    print(*v)
