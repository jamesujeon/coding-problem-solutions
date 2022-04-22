# 문제 링크: https://www.acmicpc.net/problem/6763

limit, speed = int(input()), int(input())

if speed > limit:
    speed -= limit
    fine = 100 if speed <= 20 else (270 if speed <= 30 else 500)
    print(f'You are speeding and your fine is ${fine}.')
else:
    print('Congratulations, you are within the speed limit!')
