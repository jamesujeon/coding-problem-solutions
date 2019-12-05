# 문제 링크: http://codeforces.com/problemset/problem/231/A

# n = int(input())
# isSureList = [tuple(map(int, input().split())) for i in range(n)]

# count = 0
# for isSure in isSureList:
#   if sum(isSure) >= 2:
#     count += 1

# print(count)


# 다른 버전
n = int(input())
isSureList = [tuple(map(int, input().split())) for i in range(n)]

count = sum(1 if sum(isSure) >= 2 else 0 for isSure in isSureList)

print(count)