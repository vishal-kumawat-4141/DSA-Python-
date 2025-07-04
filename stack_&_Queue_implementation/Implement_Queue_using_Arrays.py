# Implement Queue using Arrays :--->
# T.C = O(N) , S.C = O(N)
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enQueue(self, item):
        return self.items.append(item)

    def deQueue(self):
        if len(self.items) == 0:
            return "Queue is empty so we can't pop !"
        x = self.items.pop(0)
        return x

    def front(self):
        if len(self.items) == 0:
            return "Queue is empty so we don't have front !"
        return self.items[0]

    def rear(self):
        if len(self.items) == 0:
            return "Queue is empty so we don't have rear !"
        return self.items[-1]

    def size(self):
        return len(self.items)


s1 = Queue()
s1.enQueue(10)
s1.enQueue(20)
s1.enQueue(30)
s1.enQueue(40)
print(s1.front())
print(s1.rear())
print(s1.size())
print(s1.deQueue())
print(s1.front())
print(s1.is_empty())
print(s1.deQueue())
print(s1.deQueue())
print(s1.deQueue())
print(s1.is_empty())
print(s1.front())
print(s1.rear())
