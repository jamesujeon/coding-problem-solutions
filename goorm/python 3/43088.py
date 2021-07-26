# 문제 링크: https://level.goorm.io/exam/43088/%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%88%98%EC%97%B4/quiz/1

n = int(input())

fibonacci = [0, 1]
for i in range(2, n + 1):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

print(sum(fibonacci))