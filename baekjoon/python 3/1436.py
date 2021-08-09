# 문제 링크: https://www.acmicpc.net/problem/1436

N = int(input())


nums = []
i = 666
while len(nums) < N:
    if '666' in str(i):
        nums.append(i)
    i += 1


print(nums[N - 1])