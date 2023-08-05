# 문제 링크: https://www.acmicpc.net/problem/25849

amounts = [100, 50, 20, 10, 5, 1]
briefcases = [a * b for a, b in zip(amounts, list(map(int, input().split()))[::-1])]
print(amounts[briefcases.index(max(briefcases))])
