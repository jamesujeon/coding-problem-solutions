# 문제 링크: https://level.goorm.io/exam/49062/%EC%A7%84%EB%B2%95-%EB%B3%80%ED%99%98/quiz/1

N, T = input().split()


for r in range(2, 17):
    try:
        if int(T, r) == int(N):
            print(r)
            break
    except ValueError:
        pass