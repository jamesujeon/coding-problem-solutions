# 문제 링크: https://www.acmicpc.net/problem/6764

a, b, c, d = (int(input()) for _ in range(4))

if a < b < c < d:
    print('Fish Rising')
elif a > b > c > d:
    print('Fish Diving')
elif a == b == c == d:
    print('Fish At Constant Depth')
else:
    print('No Fish')
