# 문제 링크: https://www.acmicpc.net/problem/25829

v = [[0, 0], [0, 0]]
for _ in range(int(input())):
    e, v1, v2 = map(int, input().split())
    v[v1 < v2][0] += e
    v[0][1] += v1
    v[1][1] += v2

if v[0][0] > v[1][0] and v[0][1] > v[1][1]:
    print(1)
elif v[0][0] < v[1][0] and v[0][1] < v[1][1]:
    print(2)
else:
    print(0)
