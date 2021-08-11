# 문제 링크: https://www.acmicpc.net/problem/2108

from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]


nums.sort()
counts = Counter(nums).most_common(2)

results = [
    round(sum(nums) / N),
    nums[N // 2],
    (counts[1] if len(counts) > 1 and counts[0][1] == counts[1][1] else counts[0])[0],
    nums[-1] - nums[0]
]


for result in results:
    print(result)