# 문제 링크: https://www.acmicpc.net/problem/6765

k = int(input())

for s in ['*' * k + 'x' * k + '*' * k, ' ' * k + 'x' * k * 2, '*' * k + ' ' * k + '*' * k]:
    for _ in range(k):
        print(s)
