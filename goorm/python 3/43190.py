# 문제 링크: https://level.goorm.io/exam/43190/%EC%9D%80%ED%96%89-%EC%98%88%EA%B8%88-%EC%9D%B4%EC%9E%90-%EA%B5%AC%ED%95%98%EA%B8%B0/quiz/1

p, i, y = map(float, input().split())


for _ in range(int(y)):
	p += p * (i / 100)


print('{:.2f}'.format(p))
