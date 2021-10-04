# 문제 링크: https://level.goorm.io/exam/43105/%EC%86%8C%EC%9D%B8%EC%88%98-%EB%B6%84%ED%95%B4/quiz/1

n = int(input())


factors = []
for i in range(2, n + 1):
    while n % i == 0:
        factors.append(i)
        n //= i

    if n <= 1:
        break


print(' '.join(map(str, factors)))
