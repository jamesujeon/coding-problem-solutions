# 문제 링크: https://level.goorm.io/exam/43245/%EC%B5%9C%EB%8C%93%EA%B0%92/quiz/1

input()
nums = map(int, input().split())

max_num = max_index = 0
for i, num in enumerate(nums):
    if num > max_num:
        max_num = num
        max_index = i + 1

print(max_num, max_index)