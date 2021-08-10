# 문제 링크: https://level.goorm.io/exam/43273/min-%ED%95%A8%EC%88%98/quiz/1

a, b = map(int, input().split())


def min(a, b):
    return a if a < b else b

result = min(a, b)


print(result)