# 문제 링크: https://www.acmicpc.net/problem/2845

L, P = map(int, input().split())
nums = map(int, input().split())

N = L * P
nums = [num - N for num in nums]

print(' '.join(map(str, nums)))
