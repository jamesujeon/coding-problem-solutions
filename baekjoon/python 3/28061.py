# 문제 링크: https://www.acmicpc.net/problem/28061

N = int(input())
a = list(map(int, input().split()))

print(max(a[i] - N + i for i in range(N)))
