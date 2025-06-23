# # retrun the odd_even linked list:--->
# T.C = O(n) , S.C =O(1)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# make initial head node
class Solution:
    def __init__(self) -> None:
        self.head = None

    # append a node :--->
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    # tracersal every node :---->
    def traversal(self):
        if not self.head:
            print("Sll is empty")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()

    def result(self):
        if self.head is None or self.head.next is None:
            return self.head
        odd = self.head
        even = self.head.next
        even_head = even

        while even is not None and even.next is not None:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = even_head
        return


s1 = Solution()
s1.append(10)
s1.append(20)
s1.append(30)
s1.append(40)
s1.traversal()
s1.result()
s1.traversal()


# # retrun the odd_even linked list:--->
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# # make initial head node
# class Solution:
#     def __init__(self) -> None:
#         self.head = None

#     # append a node :--->
#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next is not None:
#                 current = current.next
#             current.next = new_node

#     # tracersal every node :---->
#     def traversal(self):
#         if not self.head:
#             print("Sll is empty")
#         else:
#             current = self.head
#             while current is not None:
#                 print(current.val, end=" ")
#                 current = current.next
#             print()

#     def result(self):
#         if self.head is None or self.head.next is None:
#             return self.head
#         temp = self.head
#         s = []
#         while temp.next is not None:
#             s.append(temp.val)
#             temp = temp.next.next

#         temp = self.head.next
#         while temp.next is not None:
#             s.append(temp.val)
#             temp = temp.next.next

#         temp = self.head
#         index = 0
#         while temp.next is not None:
#             temp.val = s[index]
#             index += 1
#             temp = temp.next
#         return s


# s1 = Solution()
# s1.append(10)
# s1.append(20)
# s1.append(30)
# s1.append(40)
# # s1.append(50)
# s1.traversal()
# print(s1.result())
# s1.traversal()
