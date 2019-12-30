# 문제 링크: http://codeforces.com/problemset/problem/136/A

_ = input()
p_list = list(map(int, input().split()))

result = [0] * len(p_list)
for i, p in enumerate(p_list):
  result[p - 1] = str(i + 1)
result = ' '.join(result)

print(result)