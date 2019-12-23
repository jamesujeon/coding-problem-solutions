# 문제 링크: http://codeforces.com/problemset/problem/110/A

n = input()

result = sum(1 if num in "47" else 0 for num in n)
result = "YES" if result in (4, 7) else "NO"

print(result)