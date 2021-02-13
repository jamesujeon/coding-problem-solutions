# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/68644

from itertools import combinations

def solution(numbers):
    return sorted(set(sum(nums) for nums in combinations(numbers, 2)))