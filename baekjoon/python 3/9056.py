# 문제 링크: https://www.acmicpc.net/problem/9056

for _ in range(int(input())):
    a, b = map(set, input().split())
    print('YES' if a == b else 'NO')
