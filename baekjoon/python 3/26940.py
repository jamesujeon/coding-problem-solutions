# 문제 링크: https://www.acmicpc.net/problem/26940

input()
a = list(map(int, input().split()))

print(sum(i < j for i, j in zip(a, a[1:])))
