# 문제 링크: https://www.acmicpc.net/problem/10103

s = [100, 100]
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a != b:
        s[a > b] -= max(a, b)

print(s[0])
print(s[1])
