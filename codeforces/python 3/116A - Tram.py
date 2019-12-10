# 문제 링크: http://codeforces.com/problemset/problem/116/A

from functools import reduce

passengers = [tuple(map(int, input().split())) for _ in range(int(input()))]

capacity = reduce(lambda x, y: (max(x[0], x[1] - y[0] + y[1]), x[1] - y[0] + y[1]), passengers, (0, 0))[0]

print(capacity)