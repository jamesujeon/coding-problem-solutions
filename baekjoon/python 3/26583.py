# 문제 링크: https://www.acmicpc.net/problem/26583

while True:
    try:
        nums = list(map(int, input().split()))

        result = []
        for i in range(len(nums)):
            num = nums[i]
            if i > 0:
                num *= nums[i - 1]
            if i < len(nums) - 1:
                num *= nums[i + 1]
            result.append(num)

        print(' '.join(map(str, result)))

    except:
        break
