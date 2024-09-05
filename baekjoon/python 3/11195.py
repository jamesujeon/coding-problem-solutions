# 문제 링크: https://www.acmicpc.net/problem/11195

a = [0] * 26
for i in input():
    a[ord(i) - 97] += 1

print(max(sum(i % 2 for i in a) - 1, 0))
