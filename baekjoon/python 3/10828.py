# 문제 링크: https://www.acmicpc.net/problem/10828

import sys
input = sys.stdin.readline

class Stack:
    data = []

    def push(self, x: int):
        self.data.append(x)

    def pop(self) -> int:
        return self.data.pop() if not self.empty() else -1

    def size(self) -> int:
        return len(self.data)

    def empty(self) -> bool:
        return self.size() == 0

    def top(self) -> int:
        return self.data[-1] if not self.empty() else -1

stack = Stack()
for _ in range(int(input())):
    commands = input().split()
    if commands[0] == 'push':
        stack.push(int(commands[1]))
    elif commands[0] == 'pop':
        print(stack.pop())
    elif commands[0] == 'size':
        print(stack.size())
    elif commands[0] == 'empty':
        print(1 if stack.empty() else 0)
    elif commands[0] == 'top':
        print(stack.top())