# 문제 링크: https://level.goorm.io/exam/43192/factorial-%EA%B3%84%EC%8A%B9/quiz/1

n = int(input())

result = 1
for i in range(1, n + 1):
    result *= i

print(result)