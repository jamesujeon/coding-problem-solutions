# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/76502

from collections import deque

def solution(s):
    s = deque(s)

    count = 0
    for _ in range(len(s)):
        s.rotate(-1)
        if validate(s):
            count += 1

    return count

def validate(s):
    brackets = {'(': ')', '[': ']', '{': '}'}

    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif len(stack) == 0 or brackets[stack.pop()] != ch:
            return False

    return len(stack) == 0