# 문제 링크: http://codeforces.com/problemset/problem/96/A

players = input()

result = 'YES' if '1' * 7 in players or '0' * 7 in players else 'NO'

print(result)