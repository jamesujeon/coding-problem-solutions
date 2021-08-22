# 문제 링크: https://level.goorm.io/exam/43207/%EC%B5%9C%EB%8B%A8%EA%B1%B0%EB%A6%AC/quiz/1

n = int(input())
points = list(map(int, input().split()))


print(min(points[i + 1] - points[i] for i in range(n - 1)))