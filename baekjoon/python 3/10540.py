# 문제 링크: https://www.acmicpc.net/problem/10540

p1, p2 = [101, 101], [0, 0]
for _ in range(int(input())):
    x, y = map(int, input().split())
    p1 = [min(x, p1[0]), min(y, p1[1])]
    p2 = [max(x, p2[0]), max(y, p2[1])]

print(max(p2[0] - p1[0], p2[1] - p1[1])**2)
