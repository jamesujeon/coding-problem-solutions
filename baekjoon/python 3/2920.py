# 문제 링크: https://www.acmicpc.net/problem/2920

s = input().replace(' ', '')


if s == '12345678':
    print('ascending')
elif s == '87654321':
    print('descending')
else:
    print('mixed')