# 문제 링크: https://www.acmicpc.net/problem/30031

result = 0
for _ in range(int(input())):
    i = int(input().split()[0])
    if i == 136:
        result += 1000
    elif i == 142:
        result += 5000
    elif i == 148:
        result += 10000
    elif i == 154:
        result += 50000

print(result)
