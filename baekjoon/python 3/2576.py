# 문제 링크: https://www.acmicpc.net/problem/2576

nums = [int(input()) for _ in range(7)]

odds = [num for num in nums if num % 2]
if odds:
    print(sum(odds))
    print(min(odds))
else:
    print(-1)
