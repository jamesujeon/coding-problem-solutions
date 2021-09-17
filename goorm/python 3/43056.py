# 문제 링크: https://level.goorm.io/exam/43056/가위바위보/quiz/1

inputs = list(map(int, input().split()))


input_sets = sorted(set(inputs))
if len(input_sets) == 2:
    a, b = input_sets
    print(inputs.count(a if a == 1 and b == 3 else b))
else:
    print(0)