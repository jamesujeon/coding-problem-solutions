# 문제 링크: https://www.acmicpc.net/problem/10551

f = ["`1QAZ", "2WSX", "3EDC", "4RFV5TGB", "6YHN7UJM", "8IK,", "9OL.", "0P;/-['=]"]
c = [0] * 8
for i in input():
    for j in range(8):
        if i in f[j]:
            c[j] += 1
            break

print(*c, sep='\n')
