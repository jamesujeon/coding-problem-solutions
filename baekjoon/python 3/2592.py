# 문제 링크: https://www.acmicpc.net/problem/2592

n = [int(input()) for _ in range(10)]

print(sum(n) // 10)
print(max(n, key=n.count))
