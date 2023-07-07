# 문제 링크: https://www.acmicpc.net/problem/25495

input()
prev_a = b = result = 0
for a in map(int, input().split()):
    b = b * 2 if a == prev_a else 2
    prev_a = a
    result += b
    if result >= 100:
        prev_a = b = result = 0

print(result)
