# 문제 링크: https://www.acmicpc.net/problem/5121

for k in range(1, int(input()) + 1):
    n, w = map(int, input().split())
    s = list(map(int, input().split()))

    s = [sum(s[i:i + w]) // w for i in range(n - w + 1)]
    print(f'Data Set {k}:\n{max(s) - min(s)}\n')
