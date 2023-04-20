# 문제 링크: https://www.acmicpc.net/problem/21312

nums = list(map(int, input().split()))

odds = [num for num in nums if num % 2]
if odds:
    nums = odds

result = 1
for num in nums:
    result *= num

print(result)
