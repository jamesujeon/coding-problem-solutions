# 문제 링크: https://www.acmicpc.net/problem/10101

a, b, c = sorted(int(input()) for _ in range(3))

if a + b + c == 180:
    if a == b == c:
        print('Equilateral')
    elif a == b or b == c:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')
