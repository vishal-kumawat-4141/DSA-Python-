# stack using doubly linked list :--->


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None


class Queue_using_doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.pre = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if not self.head:
            return None
        elif self.tail == self.head:
            self.head = None
            self.tail = None

        else:
            x = self.head.val
            self.head = self.head.next
            self.head = None
            return x

    def front(self):
        if not self.head:
            return "stack is empty .."
        else:
            return self.head.val

    def rear(self):
        if not self.head:
            return "stack is empty .."
        else:
            return self.tail.val

    def is_empty(self):
        return not self.head

    def tarversal(self):
        if not self.head:
            return "stack is empty"
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()


s1 = Queue_using_doubly_linked_list()
s1.enqueue(11)
s1.enqueue(12)
s1.enqueue(13)
s1.enqueue(14)
s1.tarversal()
print(s1.rear())
print(s1.front())
print(s1.head.val)
print(s1.tail.val)
print()

print(s1.dequeue())
print(s1.head.val)
print(s1.tail.val)
print()

s1.tarversal()

print(s1.head.val)
print(s1.tail.val)

print()
print(s1.front())
print(s1.rear())
print(s1.is_empty())
