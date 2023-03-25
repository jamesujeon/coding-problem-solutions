# 문제 링크: https://www.acmicpc.net/problem/6825

kg, m = float(input()), float(input())

bmi = kg / (m * m)
if bmi > 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal weight")
else:
    print("Underweight")
