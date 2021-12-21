# 문제 링크: https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        return sum(min(ticket, tickets[k] - (i > k)) for i, ticket in enumerate(tickets))