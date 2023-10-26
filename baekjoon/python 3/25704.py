# 문제 링크: https://www.acmicpc.net/problem/25704

N, P = int(input()), int(input())
print(max(int(min([P, P - 500, P * .9, P - 2000, P * .75][:N // 5 + 1])), 0))
