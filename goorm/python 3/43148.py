# 문제 링크: https://level.goorm.io/exam/43148/평균과-평균보다-큰-수/quiz/1

n = int(input())
nums = list(map(int, input().split()))


avg = sum(nums) / n
count = len([num for num in nums if num > avg])


print('{:.1f} {}'.format(avg, count))