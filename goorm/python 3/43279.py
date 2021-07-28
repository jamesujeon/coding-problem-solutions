# 문제 링크: https://level.goorm.io/exam/43279/%ED%94%BC%ED%83%80%EA%B3%A0%EB%9D%BC%EC%8A%A4-%EB%AC%B8%EC%A0%9C/quiz/1

a = b = 1
while True:
    c = 1000 - a - b
    if a**2 + b**2 == c**2:
        print(a * b * c)
        break
    elif a**2 + b**2 < c**2:
        b += 1
    else:
        a += 1
        b = 1