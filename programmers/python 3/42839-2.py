# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def solution(numbers):
    nums = set()
    for i in range(1, len(numbers) + 1):
        nums |= set(map(lambda x: int(''.join(x)), set(permutations(numbers, i))))

    nums -= set(range(2))
    for i in range(2, int(max(nums)**.5) + 1):
        nums -= set(range(i**2, max(nums) + 1, i))

    return len(nums)