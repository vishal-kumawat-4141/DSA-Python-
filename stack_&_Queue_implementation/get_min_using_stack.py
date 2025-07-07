# find get minimum from the stack in O(1) ...
# T.C = O(1) ,S .C = O(N)
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) == 0:
            self.items.append([item, item])
        else:
            mini = min(self.items[-1][1], item)
            self.items.append([item, mini])

    def pop(self):
        if len(self.items) == 0:
            return "stack is empty so don't pop you !"

        x = self.items[-1][0]
        self.items.pop()
        return x

    def top(self):
        if len(self.items) == 0:
            return "stack is empty so don't have  top item !"
        x = self.items[-1][0]
        return x

    def size(self):
        return len(self.items)

    def get_Min(self):
        if len(self.items) == 0:
            return 0
        return self.items[-1][1]


s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
print("minimum value", s1.get_Min())
print(s1.top())
print(s1.size())
print(s1.pop())
print(s1.pop())
s1.push(5)
print("minimum value", s1.get_Min())
print(s1.size())
print(s1.is_empty())
print(s1.pop())
print(s1.pop())
print(s1.is_empty())
print(s1.size())
print(s1.pop())
print(s1.top())
print("minimum value", s1.get_Min())
