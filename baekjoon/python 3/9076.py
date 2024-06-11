# 문제 링크: https://www.acmicpc.net/problem/9076

for _ in range(int(input())):
    s = sorted(map(int, input().split()))[1:-1]
    print(sum(s) if s[-1] - s[0] < 4 else 'KIN')
