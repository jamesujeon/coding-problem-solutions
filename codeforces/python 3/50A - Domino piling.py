# 문제 링크: http://codeforces.com/problemset/problem/50/A

m, n = map(int, input().split())

result = int(m * n / 2)

print(result)


# 다른 방법

# m, n = map(int, input().split())

# result = 0
# while m > 0:
#   result += n if m > 1 else int(n / 2)
#   m -= 2

# print(result)