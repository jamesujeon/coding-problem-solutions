# 문제 링크: https://www.acmicpc.net/problem/10093

A, B = sorted(map(int, input().split()))

print(max(B - A - 1, 0))
print(' '.join(map(str, range(A + 1, B))))
