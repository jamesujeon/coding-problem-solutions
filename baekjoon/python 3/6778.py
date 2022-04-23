# 문제 링크: https://www.acmicpc.net/problem/6778

antenna, eyes = (int(input()) for _ in range(2))

if antenna >= 3 and eyes <= 4:
    print('TroyMartian')
if antenna <= 6 and eyes >= 2:
    print('VladSaturnian')
if antenna <= 2 and eyes <= 3:
    print('GraemeMercurian')
