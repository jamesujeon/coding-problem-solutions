# 문제 링크: https://www.acmicpc.net/problem/5363

for _ in range(int(input())):
    w = input().split()
    print(' '.join(w[2:] + w[:2]))
