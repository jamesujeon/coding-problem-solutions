# 문제 링크: https://www.acmicpc.net/problem/9916

n = int(input())
for i in range(2, n):
    n *= i

print(str(n).count('0'))
