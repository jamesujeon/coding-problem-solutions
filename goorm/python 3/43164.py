# 문제 링크: https://level.goorm.io/exam/43164/점심은-햄버거/quiz/1

n = int(input())
eat_times = list(map(int, input().split()))
heat_times = list(map(int, input().split()))

print(sum(heat_times) + min(eat_times))