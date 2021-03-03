# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    priorities = [(i, p) for i, p in enumerate(priorities)]
    count = 0
    while priorities:
        J = priorities.pop(0)
        if any(p[1] > J[1] for p in priorities):
            priorities.append(J)
        else:
            count += 1
            if J[0] == location:
                break
    return count