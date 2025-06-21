# basic of linklist :-->
# how to make a node and next :--->
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# make initial head node
class Singlylinklist:
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

    # insert a node at any position :------>
    def insert(self, val, position):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            pervious_node = None
            count = 0
            while current is not None and count < position:
                pervious_node = current
                current = current.next
                count += 1
            pervious_node.next = new_node
            new_node.next = current

    # delete any val of node :--->

    def delete(self, val):
        temp = self.head
        if temp.next is not None:
            if temp.val == val:
                self.head = temp.next
                del temp
                return
            else:
                found = False
                previous_node = None
                while temp is not None:
                    if temp.val == val:
                        found = True
                        break
                    previous_node = temp
                    temp = temp.next
                if found:
                    previous_node.next = temp.next
                    del temp
                    return
                else:
                    print("Node is not found")


s1 = Singlylinklist()
# Node1 = Node(5)
# Node2 = Node(1)
# Node3 = Node(7)
# Node4 = Node(8)
# Node5 = Node(9)

# Node1.next = Node2
# Node2.next = Node3
# Node3.next = Node4
# print(Node5.val)
# print(Node3.next)

s1.append(11)
s1.append(12)
s1.append(13)
s1.append(14)
s1.append(15)
s1.traversal()  # 11 12 13 14 15

s1.insert(100, 0)
s1.traversal()  # 100 11 12 13 14 15

s1.delete(13)
s1.traversal()  # 100 11 12 14 15
