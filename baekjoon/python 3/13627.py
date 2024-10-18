# 문제 링크: https://www.acmicpc.net/problem/13627

N, R = map(int, input().split())
v = sorted(set(range(1, N + 1)) - set(map(int, input().split())))

print(*v if v else '*')
