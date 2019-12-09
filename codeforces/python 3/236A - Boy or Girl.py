# 문제 링크: http://codeforces.com/problemset/problem/236/A

name = input()

result = 'CHAT WITH HER!' if len(set(name)) % 2 == 0 else 'IGNORE HIM!'

print(result)