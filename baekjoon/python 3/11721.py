# 문제 링크: https://www.acmicpc.net/problem/11721

s = input()

for i in range(0, len(s), 10):
    print(s[i:i + 10])
