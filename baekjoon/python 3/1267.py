# 문제 링크: https://www.acmicpc.net/problem/1267

input()
times = list(map(int, input().split()))

plans = [(30, 10), (60, 15)]
y, m = [sum((time // plan[0] + 1) * plan[1] for time in times) for plan in plans]

print(('Y ' if y <= m else '') + ('M ' if y >= m else '') + str(min(y, m)))
