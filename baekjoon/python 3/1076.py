# 문제 링크: https://www.acmicpc.net/problem/1076

inputs = [input() for _ in range(3)]

colors = {
    'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
    'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9
}
result = (colors[inputs[0]] * 10 + colors[inputs[1]]) * (10 ** colors[inputs[2]])

print(result)
