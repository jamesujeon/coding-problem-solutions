# 문제 링크: https://www.acmicpc.net/problem/5222

for _ in range(int(input())):
    k, t = input().split()

    t = ''.join(chr((ord(t[i]) + ord(k[i % len(k)]) - 130) % 26 + 65) for i in range(len(t)))

    print(f'Ciphertext: {t}')
