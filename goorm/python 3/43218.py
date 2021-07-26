# 문제 링크: https://level.goorm.io/exam/43218/%EC%8A%A4%ED%83%9D-stack/quiz/1

class Stack:

    def __init__(self, size):
        self.list = []
        self.size = size

    def push(self, n):
        if len(self.list) < self.size:
            self.list.append(n)
        else:
            print('overflow')

    def pop(self):
        if len(self.list) > 0:
            return self.list.pop()
        else:
            print('underflow')


stack = Stack(10)
for _ in range(int(input())):
    command = input()
    if command == '0':
        stack.push(int(input()))
    elif command == '1':
        stack.pop()
    else:
        break

for n in stack.list:
    print(n, end=' ')