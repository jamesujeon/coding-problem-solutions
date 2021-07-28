# 문제 링크: https://level.goorm.io/exam/43277/%EB%B2%A1%ED%84%B0%EC%9D%98-%EC%97%B0%EC%82%B0/quiz/1

ax, ay = map(int, input().split())
bx, by = map(int, input().split())
op = input()

if op == '+':
    print('{:.2f} {:.2f}'.format(ax + bx, ay + by))
else:
    print('{:.2f} {:.2f}'.format(ax - bx, ay - by))