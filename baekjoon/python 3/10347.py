# 문제 링크: https://www.acmicpc.net/problem/10347

r = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

while (s := input()) != '0':
    n, m = s.split()
    print(''.join(r[(r.index(i) + int(n)) % 28] for i in m[::-1]))
