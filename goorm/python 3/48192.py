# 문제 링크: https://level.goorm.io/exam/48192/%ED%9A%8C%EB%AC%B8/quiz/1

inputs = [input() for _ in range(int(input()))]


def is_palindrome(s, l, r):
	while l < r:
		if s[l] != s[r]:
			return False

		l += 1
		r -= 1

	return True


def check_palindrome(s):
	l, r = 0, len(s) - 1
	while l < r:
		if s[l] != s[r]:
			if is_palindrome(s, l + 1, r) or is_palindrome(s, l, r - 1):
				return 1
			else:
				return 2

		l += 1
		r -= 1

	return 0


for s in inputs:
	print(check_palindrome(s))