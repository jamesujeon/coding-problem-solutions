# 문제 링크: https://www.acmicpc.net/problem/7599

while (s := input()) != '# 0':
    n, f = s.split()

    print(f"{n} Library")
    for i in range(1, int(input()) + 1):
        w, t = input().split()
        print(f"Book {i} {'horizontal' if len(t) * int(f) + 2 <= int(w) else 'vertical'}")
