# 문제 링크: https://www.acmicpc.net/problem/23794

N = int(input())

print('@' * (N + 2))
for _ in range(N):
    print('@' + ' ' * N + '@')
print('@' * (N + 2))
