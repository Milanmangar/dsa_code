# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# class S_LL:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0

#     def append(self, value):
#         # time=O(1), space=O(1)
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1
#         return True

#     def sort(self):
#         for _ in range(self.length):


#     def print_sll(self):
#         l = []
#         temp = self.head
#         while temp is not None:
#             l.append(temp.value)
#             temp = temp.next
#         print(l)


# s_ll = S_LL()

# # to append
# s_ll.append(25)
# s_ll.append(84)
# s_ll.append(16)
# s_ll.print_sll()
# s_ll.sort()
# s_ll.print_sll()


a = [15, 7654, 156, 342, 357, 153]
# [7654, 15, 156, 342, 357, 153]
print(a)
for i in range(len(a) - 1):
    l = len(a) - i - 1
    for j in range(l):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)
