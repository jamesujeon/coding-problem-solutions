# 문제 링크: https://level.goorm.io/exam/43161/n%EC%A7%84%EB%B2%95/quiz/1

i, n = map(int, input().split())


nums = '0123456789ABCDEFGHIJ'

result = ''
while i > 0:
	i, mod = divmod(i, n)
	result += nums[mod]

result = result[::-1]


print(result)