# 문제 링크: https://level.goorm.io/exam/43135/3%EC%9D%98-%EB%B0%B0%EC%88%98-%EA%B2%8C%EC%9E%84/quiz/1

n = int(input())


for i in range(1, n + 1):
    print(i if i % 3 else 'X', end=' ')
