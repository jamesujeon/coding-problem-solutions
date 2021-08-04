# 문제 링크: https://www.acmicpc.net/problem/10866

class Deque:
    elements = []

    def push_front(self, x: int):
        self.elements.insert(0, x)

    def push_back(self, x: int):
        self.elements.append(x)

    def pop_front(self) -> int:
        return self.elements.pop(0) if not self.empty() else -1

    def pop_back(self) -> int:
        return self.elements.pop() if not self.empty() else -1

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

deque = Deque()
for _ in range(int(input())):
    commands = input().split()
    if commands[0] == 'push_front':
        deque.push_front(int(commands[1]))
    elif commands[0] == 'push_back':
        deque.push_back(int(commands[1]))
    elif commands[0] == 'pop_front':
        print(deque.pop_front())
    elif commands[0] == 'pop_back':
        print(deque.pop_back())
    elif commands[0] == 'size':
        print(deque.size())
    elif commands[0] == 'empty':
        print(1 if deque.empty() else 0)
    elif commands[0] == 'front':
        print(deque.front())
    elif commands[0] == 'back':
        print(deque.back())