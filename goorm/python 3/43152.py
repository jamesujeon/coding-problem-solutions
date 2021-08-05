# 문제 링크: https://level.goorm.io/exam/43152/%EC%99%84%EC%A0%84-%EC%A0%9C%EA%B3%B1%EC%88%98/quiz/1

nums = [int(input()) for _ in range(int(input()))]

count = sum(int(num**.5)**2 == num for num in nums)

print(count)