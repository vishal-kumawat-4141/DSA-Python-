# reverse linked list :--->
# Method 1:---> T.C = O(2n) ~~ O(n) , S.C = O(n)
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class Solution:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next is not None:
#                 current = current.next
#             current.next = new_node

#     def traversal(self):
#         if not self.head:
#             print("sll is empty")
#         else:
#             current = self.head
#             while current is not None:
#                 print(current.val, end=" ")
#                 current = current.next
#             print()

#     def result(self):
#         temp = self.head
#         stack = []
#         while temp is not None:
#             stack.append(temp.val)
#             temp = temp.next

#         temp = self.head
#         while temp is not None:
#             e = stack.pop()
#             temp.val = e
#             temp = temp.next


# s1 = Solution()
# s1.append(10)
# s1.append(20)
# s1.append(30)
# print(s1.head.val)
# s1.result()
# s1.traversal()
# print(s1.head.val)


# Method 2:---> T.C = O(n) , S.C = O(1)
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

    def traversal(self):
        print("linked list is : ---> ")
        if not self.head:
            print("sll is empty")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()

    def result(self):
        pre = None
        temp = self.head
        while temp is not None:
            front = temp.next
            temp.next = pre
            pre = temp
            temp = front
        self.head = pre


s1 = Solution()
s1.append(10)
s1.append(20)
s1.append(30)
s1.traversal()
print("before reverse head is  :--> ", s1.head.val)
s1.result()
s1.traversal()
print("after  reverse head is :--> ", s1.head.val)
