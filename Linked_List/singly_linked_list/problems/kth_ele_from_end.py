class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True


# def find_kth_from_end(ll, index):
#     l = 0
#     temp = ll.head
#     while temp is not None:
#         l+=1
#         temp = temp.next
#     if index > l:
#         return None
#     needed_index = l - index
#     curr_index = 0
#     temp = ll.head
#     while temp is not None:
#         if curr_index == needed_index:
#             return temp
#         temp = temp.next
#         curr_index += 1
#     return None


def find_kth_from_end(ll, k):
    # 1. Initialize two pointers, 'slow' and 'fast', both pointing to the
    # starting node of the linked list.
    slow = fast = ll.head

    # 2. Move the 'fast' pointer 'k' positions ahead.
    for _ in range(k):
        # 2.1. If at any point during these 'k' movements, the 'fast'
        # pointer reaches the end of the list, then it means the list
        # has less than 'k' nodes, and thus, returning None is appropriate.
        if fast is None:
            return None

        # 2.2. Move the 'fast' pointer to the next node.
        fast = fast.next

    # 3. Now, move both 'slow' and 'fast' pointers one node at a time until
    # the 'fast' pointer reaches the end of the list. Since the 'fast' pointer
    # is already 'k' nodes ahead of the 'slow' pointer, by the time 'fast'
    # reaches the end, 'slow' will be at the kth node from the end.
    while fast:
        slow = slow.next
        fast = fast.next

    # 4. Return the 'slow' pointer, which is now pointing to the kth node
    # from the end.
    return slow


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 1
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4


"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""
