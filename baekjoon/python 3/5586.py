# 문제 링크: https://www.acmicpc.net/problem/5586

s = input()

print(s.count('JOI'))
print(sum(s[i:].startswith('IOI') for i in range(len(s) - 2)))
