# 문제 링크: http://codeforces.com/problemset/problem/116/A

from functools import reduce

passengers = [tuple(map(int, input().split())) for _ in range(int(input()))]

# count = 0
# capacity = 0
# for a, b in passengers:
#   count += b - a
#   capacity = max(capacity, count)

capacity = reduce(lambda x, y: (max(x[0], x[1] - y[0] + y[1]), x[1] - y[0] + y[1]), passengers, (0, 0))[0]

print(passengers)
print(capacity)