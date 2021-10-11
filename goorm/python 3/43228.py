# 문제 링크: https://level.goorm.io/exam/43228/%EB%91%90-%EC%A0%90-%EC%82%AC%EC%9D%B4%EC%9D%98-%EA%B1%B0%EB%A6%AC/quiz/1

points = [list(map(int, input().split())) for _ in range(2)]

distance = ((points[0][0] - points[1][0])**2 + (points[0][1] - points[1][1])**2)**.5

print('{:.2f}'.format(distance))
