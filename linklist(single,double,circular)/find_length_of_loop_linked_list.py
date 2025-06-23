# Find Length of Loop in Linked List
# Method 1 :---> T.C = O(n) , S.C = O(1)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    def result(self):
        self.head = Node1
        slow = self.head
        fast = self.head
        count = 0
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = slow.next
                count = 1
                while slow != fast:
                    slow = slow.next
                    count += 1
                return count
        return count


s1 = Solution()
Node1 = Node(10)
Node2 = Node(11)
Node3 = Node(13)
Node4 = Node(14)
Node5 = Node(15)
Node6 = Node(16)
Node7 = Node(17)
Node8 = Node(18)
Node9 = Node(19)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5
Node5.next = Node6
Node6.next = Node7
Node7.next = Node8
Node8.next = Node9
Node9.next = Node1

print(s1.result())

# method 2 :---> T.C = O(n) ,S.C =O(n)
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
#         my_dict = dict()
#         travel = 0
#         while temp is not None:
#             if temp.val in my_dict:
#                 return travel - my_dict[temp.val]
#             my_dict[temp.val] = travel
#             travel += 1
#             temp = temp.next
#         return 0


# s1 = Solution()
# Node1 = Node(10)
# Node2 = Node(11)
# Node3 = Node(13)
# Node4 = Node(14)
# Node5 = Node(15)
# Node6 = Node(16)
# Node7 = Node(17)
# Node8 = Node(18)
# Node9 = Node(19)

# Node1.next = Node2
# Node2.next = Node3
# Node3.next = Node4
# Node4.next = Node5
# Node5.next = Node6
# Node6.next = Node7
# Node7.next = Node8
# Node8.next = Node9
# Node9.next = Node4

# print(s1.result())
