# 문제 링크: https://level.goorm.io/exam/43134/%EC%A0%95%EC%9C%A1%EA%B0%81%ED%98%95%EC%9D%98-%EB%84%93%EC%9D%B4/quiz/1

n = int(input())

area = 3 * n * (n**2 - (n / 2)**2)**.5
print('{:.2f}'.format(area))