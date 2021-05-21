# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/17677

from collections import Counter

def solution(str1, str2):
    c1, c2 = convert(str1), convert(str2)
    intersection = sum((c1 & c2).values())
    union = sum((c1 | c2).values())
    return int((intersection / union if union > 0 else 1) * 65536)

def convert(s: str) -> Counter:
    s = [(s[i] + s[i + 1]).lower() for i in range(len(s) - 1)]
    return Counter(filter(str.isalpha, s))