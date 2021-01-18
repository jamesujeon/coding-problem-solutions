# 문제 링크: https://www.acmicpc.net/problem/2750

nums = []
for _ in range(int(input())):
    nums.append(int(input()))

for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

for num in nums:
    print(num)