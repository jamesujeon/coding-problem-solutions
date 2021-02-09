# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42578

from collections import defaultdict
from functools import reduce

def solution(clothes):
    cases = defaultdict(int)
    for cloth in clothes:
        cases[cloth[1]] += 1

    return reduce(lambda x, y: x * (y + 1), cases.values(), 1) - 1