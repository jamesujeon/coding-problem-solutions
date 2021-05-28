# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    limit = 10
    x = y = limit // 2
    paths = set()
    for dir in dirs:
        origin = (y, x)
        if dir == 'U':
            y = min(y + 1, limit)
        elif dir == 'D':
            y = max(y - 1, 0)
        elif dir == 'R':
            x = min(x + 1, limit)
        else:
            x = max(x - 1, 0)

        if origin != (y, x):
            paths.add(tuple(sorted([origin, (y, x)])))

    return len(paths)