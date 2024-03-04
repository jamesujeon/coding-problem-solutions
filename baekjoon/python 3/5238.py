# 문제 링크: https://www.acmicpc.net/problem/5238

for _ in range(int(input())):
    k, *s = map(int, input().split())
    print('YES' if all(s[i] == s[i - 1] + s[i - 2] for i in range(2, k)) else 'NO')
