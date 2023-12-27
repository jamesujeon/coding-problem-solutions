# 문제 링크: https://www.acmicpc.net/problem/3076

R, C = map(int, input().split())
A, B = map(int, input().split())

for i in range(R):
    for _ in range(A):
        print(''.join(('X' if i % 2 == j % 2 else '.') * B for j in range(C)))
