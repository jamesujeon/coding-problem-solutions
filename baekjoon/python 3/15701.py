# 문제 링크: https://www.acmicpc.net/problem/15701

n = int(input())
c = sum(n % i == 0 for i in range(1, int(n**.5) + 1)) * 2 - (int(n**.5)**2 == n)
print(c)
