# 문제 링크: https://level.goorm.io/exam/43064/binary-search/quiz/1

input()
nums = list(map(int, input().split()))
target = int(input())

low, mid, high = 0, (len(nums) - 1) // 2, len(nums) - 1
while low <= high and nums[mid] != target:
    if nums[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

print(mid + 1 if low <= high else 'X')