# 문제 링크: https://level.goorm.io/exam/43124/%ED%99%80%EC%88%98%EC%9D%98-%ED%95%A9/quiz/1

A, B = map(int, input().split())


print(sum(i for i in range(A, B + 1) if i % 2))