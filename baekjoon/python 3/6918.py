# 문제 링크: https://www.acmicpc.net/problem/6918

t = [int(input()) for _ in range(5)]

c = []
for p in range(t[-1] // t[0] + 1):
    i = t[-1] - t[0] * p
    for g in range(i // t[1] + 1):
        j = i - t[1] * g
        for r in range(j // t[2] + 1):
            k = j - t[2] * r
            if k % t[3] == 0:
                o = k // t[3]
                c.append((p + g + r + o, p, g, r, o))

for _, p, g, r, o in c:
    print(f"# of PINK is {p} # of GREEN is {g} # of RED is {r} # of ORANGE is {o}")
print(f"Total combinations is {len(c)}.")
print(f"Minimum number of tickets to print is {sorted(c)[0][0]}.")
