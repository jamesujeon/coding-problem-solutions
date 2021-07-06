# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/60058

def solution(p):
    if not p or is_valid(p):
        return p

    u = ''
    while not is_balanced(u):
        u = p[:len(u) + 2]
    v = p[len(u):]

    if is_valid(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + bracket_reversed(u[1:len(u) - 1])

def is_valid(p):
    count = 0
    for ch in p:
        count += 1 if ch == '(' else -1
        if count < 0:
            return False
    return count == 0

def is_balanced(p):
    return p and p.count('(') == p.count(')')

def bracket_reversed(p):
    return ''.join(')' if ch == '(' else '(' for ch in p)