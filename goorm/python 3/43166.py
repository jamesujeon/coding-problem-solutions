# 문제 링크: https://level.goorm.io/exam/43166/3%EA%B3%BC-5%EC%9D%98-%EB%B0%B0%EC%88%98/quiz/1

n = int(input())

print(sum(i for i in range(3, n + 1) if not i % 3 or not i % 5))