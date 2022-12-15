# 문제 링크: https://www.acmicpc.net/problem/10395

print("NY"[all(X != Y for X, Y in zip(input().split(), input().split()))])
