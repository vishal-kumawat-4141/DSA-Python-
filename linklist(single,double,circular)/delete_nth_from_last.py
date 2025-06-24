# delete the last nth node :---->
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class Solution:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         current = self.head
#         if not self.head:
#             self.head = new_node
#         else:
#             while current.next is not None:
#                 current = current.next
#             current.next = new_node

#     def traversal(self):
#         if not self.head:
#             print("sll is empty")
#         else:
#             temp = self.head
#             while temp is not None:
#                 print(temp.val, end=" ")
#                 temp = temp.next
#             print()

#     def delete(self, n):
#         current = self.head
#         length = 0
#         while current is not None:
#             length += 1
#             current = current.next
#         if length < n:
#             return

#         if length == n:
#             # new_head = self.head
#             # new_head = self.head.next
#             self.head = self.head.next

#         else:
#             position = length - n
#             # print("position = ", position)
#             count = 1
#             temp = self.head
#             while count < position:
#                 count += 1
#                 temp = temp.next
#             temp.next = temp.next.next


# s1 = Solution()
# s1.append(10)
# s1.append(20)
# s1.append(30)
# s1.append(40)
# s1.append(50)
# s1.append(60)
# s1.append(70)
# s1.traversal()
# s1.delete(5)
# s1.traversal()
# delete the last nth node :---->
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        current = self.head
        if not self.head:
            self.head = new_node
        else:
            while current.next is not None:
                current = current.next
            current.next = new_node

    def traversal(self):
        if not self.head:
            print("sll is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.val, end=" ")
                temp = temp.next
            print()

    def delete(self, n):
        slow = self.head
        fast = self.head
        for _ in range(n):
            fast = fast.next

        if fast == None:
            self.head = self.head.next
            return

        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next


s1 = Solution()
s1.append(10)
s1.append(20)
s1.append(30)
s1.append(40)
s1.append(50)
s1.append(60)
s1.append(70)
s1.traversal()
s1.delete(7)
s1.traversal()
