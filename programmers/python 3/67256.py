# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    def get_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    points = [
        (1, 0),
        (0, 3), (1, 3), (2, 3),
        (0, 2), (1, 2), (2, 2),
        (0, 1), (1, 1), (2, 1),
        (0, 0), (2, 0)
    ]
    thumbs = {'L': points[10], 'R': points[11]}
    answer = ''
    for n in numbers:
        point = points[n]
        thumb = ''
        if point[0] == 1:
            l_distance = get_distance(thumbs['L'], point)
            r_distance = get_distance(thumbs['R'], point)
            if l_distance == r_distance:
                thumb = 'L' if hand == 'left' else 'R'
            else:
                thumb = 'L' if l_distance < r_distance else 'R'
        else:
            thumb = 'L' if point[0] == 0 else 'R'
        thumbs[thumb] = point
        answer += thumb
    return answer