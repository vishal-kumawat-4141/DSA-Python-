#  Implement Stack using Queue :--->
from collections import deque


class stack_to_queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        for i in range(len(self.items) - 1):
            self.items.append(self.items.popleft())

    def pop(self):
        if len(self.items) == 0:
            return "stack is empty so we can't pop !"
        x = self.items.popleft()
        return x

    def top(self):
        if len(self.items) == 0:
            return "stack is empty so we don't have top !"
        return self.items[-1]

    def size(self):
        return len(self.items)


s1 = stack_to_queue()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
print(s1.top())
print(s1.size())
print(s1.pop())
print(s1.is_empty())
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.is_empty())
print(s1.top())
