# 문제 링크: https://www.acmicpc.net/problem/6795

a, b, c, d, s = (int(input()) for _ in range(5))

s1 = [1] * a + [0] * b
s2 = [1] * c + [0] * d
d = sum(s1[i % (a + b)] - s2[i % (c + d)] for i in range(s))

if d > 0:
    print('Nikky')
elif d < 0:
    print('Byron')
else:
    print('Tied')
