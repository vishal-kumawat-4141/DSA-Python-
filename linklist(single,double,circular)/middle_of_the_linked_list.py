# middle of the linked list :-->
# T.C = O(n) , S.C = O(1)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def traversal(self):
        self.count = 0
        if not self.head:
            print("Sll is empty")
        else:
            current = self.head
            while current is not None:
                self.count += 1
                print(current.val, end=" ")
                current = current.next
            print()

    def middle(self):
        result = []
        n = self.count
        if n % 2 == 0:
            mid = (n // 2) + 1
        else:
            mid = n // 2
        temp = self.head
        c = 0
        while temp is not None:
            if c >= mid:
                result.append(temp.val)
            temp = temp.next
            c += 1

        # for i in range(0, mid):
        #     temp = temp.next
        # for i in range(mid, n):
        #     print(temp.val, end=" ")
        #     temp = temp.next

        return result


s1 = Solution()
head = [1, 2, 3, 4, 5]
for i in head:
    s1.append(i)


s1.traversal()
print(s1.middle())
