# 문제 링크: https://www.acmicpc.net/problem/17009

a = (int(input()) for _ in range(3))
b = (int(input()) for _ in range(3))

a = sum(count * (3 - i) for i, count in enumerate(a))
b = sum(count * (3 - i) for i, count in enumerate(b))

if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('T')
