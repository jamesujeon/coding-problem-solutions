# 문제 링크: https://www.acmicpc.net/problem/13224

i = 0
for m in input():
    i = (- i - ord(m)) % 3

print(i + 1)
