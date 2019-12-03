# 문제 링크: http://codeforces.com/problemset/problem/1/A

import math

n, m, a = map(int, input().split())

hori_stones = math.ceil(n / a)
vert_stones = math.ceil(m / a)
result = hori_stones * vert_stones

print(result)