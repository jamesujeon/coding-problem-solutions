# 문제 링크: https://www.acmicpc.net/problem/16861

n = int(input())

while n % sum(map(int, str(n))) != 0:
    n += 1

print(n)
