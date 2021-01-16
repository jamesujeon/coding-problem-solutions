# 문제 링크: https://www.acmicpc.net/problem/11653

n = int(input())

sqrt = int(n ** .5)
i = 2
while i <= sqrt:
    while n % i == 0:
        print(i)
        n //= i
    i += 1
if n > 1:
    print(n)