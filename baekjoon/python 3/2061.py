# 문제 링크: https://www.acmicpc.net/problem/2061

K, L = map(int, input().split())

for i in range(2, L):
    if K % i == 0:
        print(f'BAD {i}')
        break
else:
    print('GOOD')
