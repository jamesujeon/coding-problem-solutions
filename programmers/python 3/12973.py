# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    if len(s) % 2:
        return 0

    stack = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    return 1 if not stack else 0