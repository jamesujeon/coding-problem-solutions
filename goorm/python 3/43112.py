# 문제 링크: https://level.goorm.io/exam/43112/%EB%84%A4-%EC%88%98%EC%9D%98-%EA%B3%B1/quiz/1

nums = list(map(int, input().split()))


def mul(a, b):
    return a * b

print(mul(mul(nums[0], nums[1]), mul(nums[2], nums[3])))