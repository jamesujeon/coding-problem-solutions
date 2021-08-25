# 문제 링크: https://level.goorm.io/exam/43182/%EA%B5%AC%EA%B5%AC%EB%8B%A8/quiz/1

n = int(input())


for a in range(2, 10):
    for b in range(1, 10):
        print(f'{a} * {b} = {a * b}', end=' ')

        if b % n == 0:
            print()