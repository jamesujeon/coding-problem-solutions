# 문제 링크: https://level.goorm.io/exam/43236/%EB%8F%88-%EA%B3%84%EC%82%B0/quiz/1

K = int(input())

nums = []
for _ in range(K):
    num = int(input())
    if num > 0:
        nums.append(num)
    else:
        nums.pop()

print(sum(nums))