# 문제 링크: https://www.acmicpc.net/problem/11605

ops = {'A': '+', 'S': '-', 'M': '*', 'D': '/'}
s = [input().split() for _ in range(int(input()))]
c = 0
for i in range(1, 101):
    for op, v in s:
        i = eval(f'i {ops[op[0]]} {int(v)}')
        if i < 0 or i % 1:
            c += 1
            break

print(c)
