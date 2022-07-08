# 문제 링크: https://www.acmicpc.net/problem/4589

groups = [list(map(int, input().split())) for _ in range(int(input()))]

print('Gnomes:')
for group in groups:
    if group == sorted(group) or group == sorted(group, reverse=True):
        print('Ordered')
    else:
        print('Unordered')
