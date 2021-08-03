# 문제 링크: https://level.goorm.io/exam/43104/%EB%B6%84%ED%95%B4%ED%95%A9/quiz/1

N = int(input())

for M in range(N - len(str(N)) * 9, N + 1):
    if M + sum(map(int, str(M))) == N:
        print(M)
        break
else:
    print(0)