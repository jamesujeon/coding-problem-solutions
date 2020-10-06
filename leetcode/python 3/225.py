# 문제 링크: https://leetcode.com/problems/implement-stack-using-queues/

from queue import Queue

class MyStack:

    def __init__(self):
        self.queue = Queue()
        self.peek = None

    def push(self, x: int) -> None:
        temp = [self.queue.get() for _ in range(self.queue.qsize())]
        self.queue.put(x)
        for element in temp:
            self.queue.put(element)
        self.peek = x

    def pop(self) -> int:
        if self.empty():
            return

        peek = self.queue.get()
        if self.empty():
            self.peek = None
        else:
            self.push(self.queue.get())
        return peek

    def top(self) -> int:
        if self.empty():
            return

        return self.peek

    def empty(self) -> bool:
        return self.queue.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()