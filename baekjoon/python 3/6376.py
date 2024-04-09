# 문제 링크: https://www.acmicpc.net/problem/6376

print('n e\n- -----------')

e, f = 0, 1
for n in range(10):
    f *= max(n, 1)
    e += 1 / f

    if n < 3:
        print(f'{n} {e:.2g}')
    else:
        print(f'{n} {e:.9f}')
