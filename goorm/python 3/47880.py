# 문제 링크: https://level.goorm.io/exam/47880/%EB%B6%80%EB%B6%84-%ED%8C%B0%EB%A6%B0%EB%93%9C%EB%A1%AC-%EB%AC%B8%EC%9E%90%EC%97%B4/quiz/1

S = input()


def is_palindrome(s, l, r):
	while l < r:
		if s[l] != s[r]:
			return False

		l += 1
		r -= 1

	return True


max_length = 0
for l in range(len(S)):
	for i in range(len(S) - l):
		if is_palindrome(S, i, i + l):
			max_length = l + 1
			break

print(max_length)