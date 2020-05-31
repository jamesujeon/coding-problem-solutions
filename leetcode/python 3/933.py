# 문제 링크: https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.pings = []

    def ping(self, t: int) -> int:
        self.pings.append(t)
        while self.pings[0] < t - 3000:
            self.pings.pop(0)
        return len(self.pings)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
