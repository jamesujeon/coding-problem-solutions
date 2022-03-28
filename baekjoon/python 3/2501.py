# 문제 링크: https://www.acmicpc.net/problem/2501

n, k = map(int, input().split())

for i in range(1, n + 1):
    if n % i == 0:
        k -= 1
        if k == 0:
            print(i)
            break
if k > 0:
    print(0)
