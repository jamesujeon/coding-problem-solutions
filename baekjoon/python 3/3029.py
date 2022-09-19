# 문제 링크: https://www.acmicpc.net/problem/3029

def get_time():
    h, m, s = map(int, input().split(':'))
    return h * 3600 + m * 60 + s

t1, t2 = get_time(), get_time()
if t1 >= t2:
    t2 += 24 * 3600

t = t2 - t1
print(f'{t // 3600:02d}:{(t % 3600) // 60:02d}:{t % 60:02d}')
