# 문제 링크: https://www.acmicpc.net/problem/11158

for _ in range(int(input())):
    s = input().split()
    print(sum(i in ['u', 'ur'] or 'lol' in i or (i in ['would', 'should'] and j == 'of') for i, j in zip(s, s[1:] + [''])) * 10)
