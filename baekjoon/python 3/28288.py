# 문제 링크: https://www.acmicpc.net/problem/28288

days = [0] * 5
for _ in range(int(input())):
    for i, y in enumerate(input()):
        if y == 'Y':
            days[i] += 1

print(','.join(str(i + 1) for i in range(5) if days[i] == max(days)))
