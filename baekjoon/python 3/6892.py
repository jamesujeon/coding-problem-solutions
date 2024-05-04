# 문제 링크: https://www.acmicpc.net/problem/6892

for _ in range(int(input())):
    w = [input() for _ in range(3)]

    is_fix_free = not any(
        w[(i + 1) % 3].startswith(w[i]) or w[(i + 1) % 3].endswith(w[i]) or
        w[(i + 2) % 3].startswith(w[i]) or w[(i + 2) % 3].endswith(w[i])
        for i in range(3)
    )

    print("Yes" if is_fix_free else "No")
