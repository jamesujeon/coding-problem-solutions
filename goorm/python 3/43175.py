# 문제 링크: https://level.goorm.io/exam/43175/%EB%B0%98%EB%B3%B5%EB%90%98%EB%8A%94-%EC%88%AB%EC%9E%90%EA%B0%80-%EC%97%86%EB%8A%94-%EC%88%98/quiz/1

n = int(input())


count = num = 0
while count < n:
	num += 1
	if len(str(num)) == len(set(str(num))):
		count += 1


print(num)