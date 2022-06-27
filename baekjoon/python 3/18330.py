# 문제 링크: https://www.acmicpc.net/problem/18330

n, k = int(input()), int(input())

print(min(n, k + 60) * 1500 + max(n - k - 60, 0) * 3000)
