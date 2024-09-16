# 문제 링크: https://www.acmicpc.net/problem/11636

for _ in range(int(input())):
    s = list(map(int, input().split()))
    print(sum(max(s[i + 1] - s[i] * 2, 0) for i in range(len(s) - 1)))
