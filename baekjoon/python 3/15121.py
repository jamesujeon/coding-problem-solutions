# 문제 링크: https://www.acmicpc.net/problem/15121

s = int(input())

print(f'{s}:')
for i in range(2, s // 2 + 2):
    for j in (i - 1, i):
        if s % (i + j) in (0, i):
            print(f'{i},{j}')
