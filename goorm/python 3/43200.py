# 문제 링크: https://level.goorm.io/exam/43200/%EC%8A%A4%ED%85%8C%EC%9D%B8-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98/quiz/1

n1, n2 = map(int, input().split())


a = 0
while ~(n1 | n2) & 1:
	a += 1
	n1 >>= 1
	n2 >>= 1

while n1 and n2:
	while ~n1 & 1:
		n1 >>= 1
	while ~n2 & 1:
		n2 >>= 1

	if n1 > n2:
		n1 -= n2
	else:
		n2 -= n1

gcd = max(n1, n2) << a


print(gcd)