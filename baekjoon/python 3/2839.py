# 문제 링크: https://www.acmicpc.net/problem/2839

n = int(input())

count = -1
for five_bags in reversed(range(n // 5 + 1)):
    m = n - (5 * five_bags)
    if m % 3 == 0:
        count = five_bags + m // 3
        break

print(count)
