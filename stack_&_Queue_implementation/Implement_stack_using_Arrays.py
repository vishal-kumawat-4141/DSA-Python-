# Implement Stack using Arrays :---->
# T.C = O(1) , S.C = O(n) n is stack space
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return "stack is empty so don't pop you !"
        x = self.items.pop()
        return x

    def top(self):
        if len(self.items) == 0:
            return "stack is empty so don't have  top item !"
        x = self.items[-1]
        return x

    def size(self):
        return len(self.items)


s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
print(s1.top())
print(s1.size())
print(s1.pop())
print(s1.pop())
print(s1.size())
print(s1.is_empty())
print(s1.pop())
print(s1.pop())
print(s1.is_empty())
print(s1.size())
print(s1.pop())
print(s1.top())
