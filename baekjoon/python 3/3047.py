# 문제 링크: https://www.acmicpc.net/problem/3047

nums = sorted(map(int, input().split()))
order = input()

print(' '.join(str(nums[ord(ch) - 65]) for ch in order))
