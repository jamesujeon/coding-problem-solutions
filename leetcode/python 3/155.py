# 문제 링크: https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min = x if self.min is None else min(self.min, x)

    def pop(self) -> None:
        self.stack.pop()
        self.min = min(self.stack) if self.stack else None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()