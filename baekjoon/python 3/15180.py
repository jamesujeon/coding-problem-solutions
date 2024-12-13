# 문제 링크: https://www.acmicpc.net/problem/15180

v = [int(input())]
while (s := input()) != '#':
    v.append((v[-1] + int(s[1]) * (1 - 2 * (s[0] == 'A'))) % 8 or 8)

print(*v, end='')
print(' reject' * (len(v) < 5 or len(v) != len(set(v))))
