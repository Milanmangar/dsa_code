import copy


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.length = 0

    # # this is for index starting with 0
    # def reverse_between(self, start_index, end_index):
    #     if self.head is None:
    #         return

    #     start_node_prev = None
    #     start_node = None
    #     end_node = None
    #     end_node_after = None
    #     curr_node = self.head
    #     prev = None
    #     for curr_index in range(end_index + 1):
    #         if curr_index == start_index:
    #             start_node = curr_node
    #             start_node_prev = prev
    #         if curr_index == end_index:
    #             end_node = curr_node
    #             end_node_after = curr_node.next
    #             break
    #         prev = curr_node
    #         curr_node = curr_node.next

    #     before = None
    #     after = start_node
    #     curr_node = start_node
    #     rev_head = None
    #     # after reversel of needed range of linked list
    #     #  start_node becomes end of the node, before becomes start of the node
    #     while curr_node:
    #         after = curr_node.next
    #         curr_node.next = before
    #         before = curr_node
    #         curr_node = after
    #         if before == end_node:
    #             rev_head = before
    #             break

    #     if start_node_prev is None:
    #         start_node.next = end_node_after
    #         self.head = rev_head
    #         return self.head
    #     start_node.next = end_node_after
    #     start_node_prev.next = rev_head
    #     return self.head

    # # this is for index starting with 1
    # def reverse_between(self, start_index, end_index):
    #     if self.head is None:
    #         return

    #     start_node_prev = None
    #     start_node = None
    #     end_node = None
    #     end_node_after = None
    #     curr_node = self.head
    #     prev = None
    #     for curr_index in range(1, end_index + 1):
    #         if curr_index == start_index:
    #             start_node = curr_node
    #             start_node_prev = prev
    #         if curr_index == end_index:
    #             end_node = curr_node
    #             end_node_after = curr_node.next
    #             break
    #         prev = curr_node
    #         curr_node = curr_node.next

    #     before = None
    #     after = start_node
    #     curr_node = start_node
    #     rev_head = None
    #     # after reversel of needed range of linked list
    #     #  start_node becomes end of the node, before becomes start of the node
    #     while curr_node:
    #         after = curr_node.next
    #         curr_node.next = before
    #         before = curr_node
    #         curr_node = after
    #         if before == end_node:
    #             rev_head = before
    #             break

    #     if start_node_prev is None:
    #         start_node.next = end_node_after
    #         self.head = rev_head
    #         return self.head
    #     start_node.next = end_node_after
    #     start_node_prev.next = rev_head
    #     return self.head

    # this is for index starting with 1
    def reverse_between(self, start_index, end_index):
        if self.head is None:
            return

        start_node_prev = None
        prev = None

        before = None
        curr_node = self.head
        after = self.head

        rev_head = None
        rev_tail = None
        curr_index = 1
        while curr_node:
            if curr_index >= start_index and curr_index <= end_index:
                if curr_index == start_index:
                    start_node_prev = prev
                    rev_tail = curr_node
                after = curr_node.next
                curr_node.next = before
                before = curr_node
                curr_node = after
                if curr_index == end_index:
                    rev_head = before
                    rev_tail.next = after
                    break
            else:
                prev = curr_node
                curr_node = curr_node.next
            curr_index += 1

        if start_node_prev is None:
            self.head = rev_head
            return self.head
        start_node_prev.next = rev_head
        return self.head


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# # Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# # Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# # Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty()
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


linked_list = LinkedList(21)

print("Original linked list: ")
linked_list.print_list()

linked_list.reverse_between(1, 1)
print("Reversed sublist (1, 1): ")
linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None
    
"""
