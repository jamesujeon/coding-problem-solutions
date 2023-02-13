# 문제 링크: https://www.acmicpc.net/problem/5342

chart = {
    "Paper": 57.99,
    "Printer": 120.50,
    "Planners": 31.25,
    "Binders": 22.50,
    "Calendar": 10.95,
    "Notebooks": 11.20,
    "Ink": 66.95
}

cost = 0
while True:
    item = input()
    if item == "EOI":
        break

    cost += chart[item]

print(f'${cost}')
