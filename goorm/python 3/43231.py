# 문제 링크: https://level.goorm.io/exam/43231/%EB%A9%80%ED%8B%B0%ED%83%AD-%EC%82%AC%EC%9A%A9/quiz/1

N = int(input())
holes = map(int, input().split())


print(sum(holes) - (N - 1))