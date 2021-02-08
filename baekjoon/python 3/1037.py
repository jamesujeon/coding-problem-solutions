# 문제 링크: https://www.acmicpc.net/problem/1037

input()
nums = list(map(int, input().split()))

print(min(nums) * max(nums))