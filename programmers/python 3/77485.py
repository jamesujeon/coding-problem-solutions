# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    array = [[j + 1 + columns * i for j in range(columns)] for i in range(rows)]
    min_nums = []

    for query in queries:
        x1, y1, x2, y2 = map(lambda x: x - 1, query)
        min_num = first = array[x1][y1]

        for i in range(x1, x2):
            array[i][y1] = array[i + 1][y1]
            min_num = min(array[i][y1], min_num)
        for j in range(y1, y2):
            array[x2][j] = array[x2][j + 1]
            min_num = min(array[x2][j], min_num)
        for i in range(x2, x1, -1):
            array[i][y2] = array[i - 1][y2]
            min_num = min(array[i][y2], min_num)
        for j in range(y2, y1, -1):
            array[x1][j] = array[x1][j - 1]
            min_num = min(array[x1][j], min_num)
        array[x1][y1 + 1] = first

        min_nums.append(min_num)

    return min_nums