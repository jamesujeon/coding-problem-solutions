# 문제 링크: https://level.goorm.io/exam/43232/%EC%95%BD%EC%88%98%EC%9D%98-%ED%95%A9/quiz/1

n = int(input())

result = sum(i for i in range(1, n + 1) if n % i == 0)

print(result)