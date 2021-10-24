# 문제 링크: https://level.goorm.io/exam/43243/bubble-sort/quiz/1

n = int(input())
nums = list(map(int, input().split()))


for i in range(1, n):
	for j in range(n - i):
		if nums[j] > nums[j + 1]:
			nums[j], nums[j + 1] = nums[j + 1], nums[j]


for num in nums:
	print(num, end=' ')