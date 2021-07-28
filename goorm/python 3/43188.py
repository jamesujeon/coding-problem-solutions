# 문제 링크: https://level.goorm.io/exam/43188/%EC%9D%B4%EC%B0%A8-%EB%B0%A9%EC%A0%95%EC%8B%9D%EC%9D%98-%ED%95%B4/quiz/1

a, b, c = map(int, input().split())

d = b**2 - 4 * a * c
if d > 0:
    x1, x2 = (-b + d**.5) / (2 * a), (-b - d**.5) / (2 * a)
    print('{:.2f}, {:.2f}'.format(x1, x2))
elif d == 0:
    x = -b / (2 * a)
    print('{:.2f}'.format(x))
else:
    print('X')