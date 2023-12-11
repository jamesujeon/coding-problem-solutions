# 문제 링크: https://www.acmicpc.net/problem/2747

n = int(input())

f = [0, 1]
for i in range(n - 1):
    f.append(f[-1] + f[-2])

print(f[-1])
