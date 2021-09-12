# 문제 링크: https://level.goorm.io/exam/49087/%EC%97%AC%EB%A6%84%EC%9D%98-%EB%8C%80%EC%82%BC%EA%B0%81%ED%98%95/quiz/1

p = [list(map(int, input().split())) for _ in range(3)]


s = abs(p[0][0] * p[1][1] + p[1][0] * p[2][1] + p[2][0] * p[0][1]
    - (p[0][0] * p[2][1] + p[1][0] * p[0][1] + p[2][0] * p[1][1])) * .5


print('{:.2f}'.format(s))
