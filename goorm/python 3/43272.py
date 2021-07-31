# 문제 링크: https://level.goorm.io/exam/43272/%ED%8C%8C%EB%8F%84%EB%B0%98-%EC%88%98%EC%97%B4/quiz/1

n = int(input())

p = [0, 1, 1, 1, 2, 2]
for i in range(6, max(n, 5) + 1):
    p.append(p[i - 1] + p[i - 5])

print(p[n])