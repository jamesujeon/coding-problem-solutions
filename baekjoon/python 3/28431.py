# 문제 링크: https://www.acmicpc.net/problem/28431

s = [int(input()) for _ in range(5)]

for i in set(s):
    if s.count(i) % 2:
        print(i)
        break
