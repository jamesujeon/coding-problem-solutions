# 문제 링크: https://www.acmicpc.net/problem/27130

a, b = int(input()), int(input())

print(a)
print(b)
for d in str(b)[::-1]:
    print(a * int(d))
print(a * b)
