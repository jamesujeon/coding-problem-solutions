# 문제 링크: https://www.acmicpc.net/problem/1149

costs = [tuple(map(int, input().split())) for _ in range(int(input()))]

min_costs = [costs[0]]
for i in range(1, len(costs)):
  min_costs.append((
    costs[i][0] + min(min_costs[i - 1][1], min_costs[i - 1][2]),
    costs[i][1] + min(min_costs[i - 1][0], min_costs[i - 1][2]),
    costs[i][2] + min(min_costs[i - 1][0], min_costs[i - 1][1])
  ))

print(min(min_costs[-1]))