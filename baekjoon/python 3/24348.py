# 문제 링크: https://www.acmicpc.net/problem/24348

a, b, c = sorted(map(int, input().split()))

print(max(a + b * c, c))
