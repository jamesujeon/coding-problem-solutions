# 문제 링크: https://level.goorm.io/exam/43256/%EC%A0%84%EA%B5%AD%EC%9D%BC%EC%A3%BC/quiz/1

n = int(input())
money = [int(input()) for _ in range(n)]


avg = sum(money) // n
result = sum(abs(m - avg) for m in money) // 2


print(result)