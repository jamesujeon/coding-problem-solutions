# 문제 링크: https://www.acmicpc.net/problem/27159

input()
result = prev = 0
for x in map(int, input().split()):
    if x - prev > 1:
        result += x
    prev = x

print(result)
