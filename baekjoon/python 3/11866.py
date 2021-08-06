# 문제 링크: https://www.acmicpc.net/problem/11866

N, K = map(int, input().split())


nums = list(range(1, N + 1))
permutaion = []

i = 0
while nums:
    i += K - 1
    if i >= len(nums):
        i %= len(nums)

    permutaion.append(nums.pop(i))


print(f"<{', '.join(map(str, permutaion))}>")