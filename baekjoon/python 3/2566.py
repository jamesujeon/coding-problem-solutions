# 문제 링크: https://www.acmicpc.net/problem/2566

max_value = max_i = max_j = 0
for i in range(9):
    for j, value in enumerate(map(int, input().split())):
        if value > max_value:
            max_value, max_i, max_j = value, i, j

print(max_value)
print(max_i + 1, max_j + 1)
