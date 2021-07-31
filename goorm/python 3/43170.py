# 문제 링크: https://level.goorm.io/exam/43170/%EC%9C%A0%EC%9D%BC%ED%95%9C-%EC%88%98/quiz/1

input()
nums = map(int, input().split())

counts = {}
for num in nums:
    if not num in counts:
        counts[num] = 0
    counts[num] += 1

for k, v in counts.items():
    if v == 1:
        print(k)
        break