# 문제 링크: https://level.goorm.io/exam/43083/%EA%B3%84%EB%8B%A8-%EC%98%A4%EB%A5%B4%EA%B8%B0/quiz/1

n = int(input())

steps = [0, 1, 2]
for i in range(3, max(n, 3) + 1):
    steps.append(steps[i - 1] + steps[i - 2])

print(steps[n])