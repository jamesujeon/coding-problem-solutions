# 문제 링크: https://www.acmicpc.net/problem/20673

p, q = int(input()), int(input())

if p <= 50 and q <= 10:
    print('White')
elif q > 30:
    print('Red')
else:
    print('Yellow')
