# 문제 링크: https://www.acmicpc.net/problem/10174

for _ in range(int(input())):
    s = input().lower()
    print('Yes' if s == s[::-1] else 'No')
