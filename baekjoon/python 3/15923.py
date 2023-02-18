# 문제 링크: https://www.acmicpc.net/problem/15923

x_list = []
y_list = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

print((max(x_list) - min(x_list) + max(y_list) - min(y_list)) * 2)
