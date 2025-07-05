# implement of queue using stack :---->
# T.C = O(N) , S.C = O(N)
class Queue_to_stack:
    def __init__(self):
        self.st1 = []
        self.st2 = []

    def enQueue(self, item):
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(item)
        while self.st2:
            self.st1.append(self.st2.pop())

    def deQueue(self):
        while not self.st1:
            print("Stack is Empty ...")
            return -1
        top_element = self.st1.pop()
        return top_element

    def front(self):
        while not self.st1:
            return "stack is Empty ..."
        return self.st1[-1]

    def rear(self):
        while not self.st1:
            return "stack is Empty ..."
        return self.st1[0]

    def is_empty(self):
        return not self.st1

    def size(self):
        while not self.st1:
            return "stack is Empty ..."
        return len(self.st1)

    def show(self):
        return self.st1


s1 = Queue_to_stack()
s1.enQueue(10)
s1.enQueue(20)
s1.enQueue(30)
s1.enQueue(40)
print(s1.st1)
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
