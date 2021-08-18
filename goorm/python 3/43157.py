# 문제 링크: https://level.goorm.io/exam/43157/%EC%A3%BC%EC%82%AC%EC%9C%84-%EB%86%80%EC%9D%B4/quiz/1

n = int(input())


for i in range(max(n - 6, 1), min(n, 7)):
    print(i, n - i)