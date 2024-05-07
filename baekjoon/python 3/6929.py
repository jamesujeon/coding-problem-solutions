# 문제 링크: https://www.acmicpc.net/problem/6929

H = int(input())

r = range(1, H + 1, 2)
for i in r:
    print('*' * i + ' ' * (H - i) * 2 + '*' * i)
for i in r[:-1][::-1]:
    print('*' * i + ' ' * (H - i) * 2 + '*' * i)
