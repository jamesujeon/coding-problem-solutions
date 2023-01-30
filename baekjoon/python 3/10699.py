# 문제 링크: https://www.acmicpc.net/problem/10699

from datetime import datetime, timezone, timedelta

print(datetime.now(timezone(timedelta(hours=9))).strftime("%Y-%m-%d"))
