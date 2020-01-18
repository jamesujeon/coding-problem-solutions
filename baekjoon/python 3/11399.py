# 문제 링크: https://www.acmicpc.net/problem/11399

n = int(input())
p = sorted(list(map(int, input().split())))

min_sum = sum(sum(p[:i + 1]) for i in range(n))
print(min_sum)
