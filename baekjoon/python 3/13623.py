# 문제 링크: https://www.acmicpc.net/problem/13623

a, b, c = map(int, input().split())

if a != b == c:
    print('A')
elif a != b != c:
    print('B')
elif a == b != c:
    print('C')
else:
    print('*')
