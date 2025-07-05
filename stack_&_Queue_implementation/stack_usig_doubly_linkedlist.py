# stack using doubly linked list :--->


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None


class Stack_using_doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.pre = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if not self.head:
            return None
        elif self.tail == self.head:
            self.head = None
            self.tail = None

        else:
            x = self.tail.val
            self.tail = self.tail.pre
            self.tail.next = None
            return x

    def top(self):
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


s1 = Stack_using_doubly_linked_list()
s1.push(11)
s1.push(12)
s1.push(13)
s1.push(14)
s1.tarversal()
print(s1.top())
print(s1.head.val)
print(s1.tail.val)
print()

print(s1.pop())
print(s1.head.val)
print(s1.tail.val)
print()

s1.tarversal()

print(s1.head.val)
print(s1.tail.val)

print()
print(s1.top())
print(s1.is_empty())
