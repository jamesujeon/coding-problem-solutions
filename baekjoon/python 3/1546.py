# 문제 링크: https://www.acmicpc.net/problem/1546

input()
n = list(map(int, input().split()))
print(sum(n) * 100 / max(n) / len(n))