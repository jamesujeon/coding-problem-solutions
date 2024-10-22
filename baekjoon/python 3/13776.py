# 문제 링크: https://www.acmicpc.net/problem/13776

s = ''
for _ in range(int(input())):
    for c in input().replace(' ', ''):
        if c not in s:
            s += c

print(s)
