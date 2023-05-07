# 문제 링크: https://www.acmicpc.net/problem/21603

N, K = map(int, input().split())

k1, k2 = K % 10, (K * 2) % 10
nums = [i for i in range(1, N + 1) if i % 10 != k1 and i % 10 != k2]

print(len(nums))
if nums:
    print(' '.join(map(str, nums)))
