# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations

def solution(nums):
    return sum(is_prime(sum(comb)) for comb in combinations(nums, 3))

def is_prime(num):
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return num > 1