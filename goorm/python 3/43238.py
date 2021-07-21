# 문제 링크: https://level.goorm.io/exam/43238/%EC%86%8C%EC%88%98-%ED%8C%90%EB%B3%84/quiz/1

def is_prime(n: int) -> bool:
	for i in range(2, int(n**.5) + 1):
		if n % i == 0:
			return False
	return n > 1

user_input = int(input())
print(str(is_prime(user_input)))