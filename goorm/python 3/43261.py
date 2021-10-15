# 문제 링크: https://level.goorm.io/exam/43261/%EB%B2%94%EC%9C%84-%EB%82%B4%EC%9D%98-%EC%88%AB%EC%9E%90%EB%A5%BC-%EB%B6%84%ED%95%B4%ED%95%98%EC%97%AC-%EA%B3%B1%ED%95%9C-%ED%9B%84-%ED%95%A9-%EA%B5%AC%ED%95%98%EA%B8%B0/quiz/1

from functools import reduce

a, b = map(int, input().split())

result = sum(reduce(lambda a, b: a * b, map(int, str(i)), 1) for i in range(a, b + 1))

print(result)