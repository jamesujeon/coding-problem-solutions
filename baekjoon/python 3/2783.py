# 문제 링크: https://www.acmicpc.net/problem/2783

X, Y = map(int, input().split())
price = 1000 / Y * X

for _ in range(int(input())):
    X, Y = map(int, input().split())
    price = min(1000 / Y * X, price)

print(f'{price:.2f}')
