# 문제 링크: https://level.goorm.io/exam/49085/t%EC%84%B8%ED%8F%AC/quiz/1

N = int(input())


times = []
minute = 0
while N > 0:
    if N % 2:
        times.append(minute)
    N //= 2
    minute += 1


print(len(times))
print(' '.join(map(str, times)))
