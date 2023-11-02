# 문제 링크: https://www.acmicpc.net/problem/1440

count = 0
for i in map(int, input().split(':')):
    if 0 < i < 13:
        count += 1
    elif i > 59:
        count = 0
        break

print(count * 2)
