# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def solution(numbers):
    n = 10**len(numbers) - 1
    primes = [False] * 2 + [True] * (n - 1)
    for i in range(2, int(n**.5) + 1):
        if primes[i]:
            for j in range(i**2, n + 1, i):
                primes[j] = False

    nums = set()
    for i in range(1, len(numbers) + 1):
        nums |= set(map(lambda x: int(''.join(x)), set(permutations(numbers, i))))
    return sum(primes[num] for num in nums)