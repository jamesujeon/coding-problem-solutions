# 문제 링크: https://www.acmicpc.net/problem/10845

class Queue:
    elements = []

    def push(self, x: int):
        self.elements.append(x)

    def pop(self) -> int:
        return self.elements.pop(0) if not self.empty() else -1

    def size(self) -> int:
        return len(self.elements)

    def empty(self) -> bool:
        return self.size() == 0

    def front(self) -> int:
        return self.elements[0] if not self.empty() else -1

    def back(self) -> int:
        return self.elements[-1] if not self.empty() else -1


import sys
input = sys.stdin.readline

queue = Queue()
for _ in range(int(input())):
    commands = input().split()
    if commands[0] == 'push':
        queue.push(int(commands[1]))
    elif commands[0] == 'pop':
        print(queue.pop())
    elif commands[0] == 'size':
        print(queue.size())
    elif commands[0] == 'empty':
        print(1 if queue.empty() else 0)
    elif commands[0] == 'front':
        print(queue.front())
    elif commands[0] == 'back':
        print(queue.back())