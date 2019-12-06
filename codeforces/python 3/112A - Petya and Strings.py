# 문제 링크: http://codeforces.com/problemset/problem/112/A

strs = [input().lower() for _ in range(2)]

result = 0 if strs[0] == strs[1] else (1 if strs[0] > strs[1] else -1)

print(result)