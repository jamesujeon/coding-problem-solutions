# 문제 링크: https://www.acmicpc.net/problem/5370

while True:
    try:
        n = bin(int(input()))[2:]
        n = n.count('0') - n.count('1')
        if n > 0:
            print('left')
        elif n < 0:
            print('right')
        else:
            print('straight')

    except:
        break
