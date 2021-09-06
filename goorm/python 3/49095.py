# 문제 링크: https://level.goorm.io/exam/49095/%EA%B3%A0%EC%9E%A5%EB%82%9C-%EC%BB%B4%ED%93%A8%ED%84%B0/quiz/1

N, c = map(int, input().split())
t = list(map(int, input().split()))


count = 1
for i in range(1, N):
    if t[i] - t[i - 1] <= c:
        count += 1
    else:
        count = 1


print(count)
