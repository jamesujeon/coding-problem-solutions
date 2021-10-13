# 문제 링크: https://level.goorm.io/exam/43167/%EB%93%B1%EC%B0%A8-%EB%98%90%EB%8A%94-%EB%93%B1%EB%B9%84-%EC%88%98%EC%97%B4/quiz/1

nums = list(map(int, input().split()))

if nums[1] - nums[0] == nums[2] - nums[1]:
	print(nums[-1] + (nums[1] - nums[0]))
else:
	print(nums[-1] * (nums[1] // nums[0]))