# linked list cycle :--> true and false
# method 1:----> T.C = O(n) , S.C = O(n)
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class Solution:
#     def __init__(self):
#         self.head = None

#     def result(self):
#         self.head = Node1
#         temp = self.head
#         myset = set()
#         while temp is not None:
#             if temp not in myset:
#                 myset.add(temp)
#                 temp = temp.next
#             else:
#                 return True
#         return False


# s1 = Solution()
# Node1 = Node(10)
# Node2 = Node(11)
# Node3 = Node(13)
# Node4 = Node(15)

# Node1.next = Node2
# Node2.next = Node3
# Node3.next = Node4
# Node4.next = Node1
# print(s1.result())


# linked list cycle :--> true and false
# Method 2 :---> T.C = O(n) , S.C = O(1)
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class Solution:
#     def __init__(self):
#         self.head = None

#     def result(self):
#         self.head = Node1
#         slow = self.head
#         fast = self.head
#         while fast is not None and fast.next is not None:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return True
#         return False


# s1 = Solution()
# Node1 = Node(10)
# Node2 = Node(11)
# Node3 = Node(13)
# Node4 = Node(15)

# Node1.next = Node2
# Node2.next = Node3
# Node3.next = Node4
# Node4.next = Node1
# print(s1.result())


# linked list cycle :--> true and false
# Method 2 :---> T.C = O(n) , S.C = O(1)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def make_cycle(self):
        a = self.head
        current = self.head
        while current is not None:
            current = current.next
            if current.next is None:
                current.next = a
                return

    def hasCycle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


s1 = Solution()
s1.append(10)
s1.append(20)
s1.append(30)
s1.make_cycle()
print(s1.hasCycle())
