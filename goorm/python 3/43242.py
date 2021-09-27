# 문제 링크: https://level.goorm.io/exam/43242/거스름돈/quiz/1

change = 1000 - int(input())


counts = []
for coin in (500, 100, 50, 10):
    counts.append(change // coin)
    change %= coin


for count in counts:
    print(count, end=' ')