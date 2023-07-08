# 문제 링크: https://www.acmicpc.net/problem/25629

N = int(input())
evens = sum(a % 2 == 0 for a in map(int, input().split()))

print(int(evens == N // 2))
