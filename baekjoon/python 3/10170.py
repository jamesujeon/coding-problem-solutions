# 문제 링크: https://www.acmicpc.net/problem/10170

titles = ("NFC West", "NFC North")
rankings = (
    (("Seattle", 13, 3, 0), ("San Francisco", 12, 4, 0), ("Arizona", 10, 6, 0), ("St. Louis", 7, 9, 0)),
    (("Green Bay", 8, 7, 1), ("Chicago", 8, 8, 0), ("Detroit", 7, 9, 0), ("Minnesota", 5, 10, 1))
)

for i in range(2):
    print(f"{titles[i]: <15}W   L  T")
    print("-----------------------")
    for j in range(4):
        ranking = rankings[i][j]
        print(f"{ranking[0]: <15}{ranking[1]: <3}{ranking[2]: >2}{ranking[3]: >3}")
    print()
