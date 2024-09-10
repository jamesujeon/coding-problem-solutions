# 문제 링크: https://www.acmicpc.net/problem/11531

ps = {}
while (s := input()) != '-1':
    m, p, r = s.split()
    if p not in ps:
        ps[p] = (r, 0)
    ps[p] = (r, ps[p][1] + (int(m) if r == 'right' else 20))

ps = [m for r, m in ps.values() if r == 'right']

print(len(ps), sum(ps))
