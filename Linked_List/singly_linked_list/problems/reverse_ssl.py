import copy


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class S_LL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        # time=O(1), space=O(1)
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # def reverse(self):
    #     actual_head = self.head
    #     temp = self.head
    #     # self.head = self.tail
    #     # self.tail = temp
    #     before = None
    #     after = temp.next
    #     for _ in range(self.length):
    #         after = temp.next
    #         temp.next = before
    #         before = temp
    #         temp = after
    #     self.head = before
    #     self.tail = actual_head
    #     return True

    # def reverse(self):
    #     if self.head is None:
    #         return None
    #     reversed_ll = None
    #     reversed_ll_head = None
    #     curr_node = self.head
    #     while curr_node:
    #         curr_node_copy = copy.deepcopy(curr_node)
    #         if reversed_ll is None:
    #             reversed_ll = curr_node_copy
    #             reversed_ll.next = None
    #         else:
    #             curr_node_copy.next = reversed_ll_head
    #         reversed_ll_head = curr_node_copy
    #         curr_node = curr_node.next
    #     self.head = reversed_ll_head
    #     return self.head

    def reverse(self):
        if self.head is None:
            return None
        before = None
        curr_node = self.head
        after = curr_node
        self.head = self.tail
        self.tail = curr_node
        while curr_node:
            after = curr_node.next
            curr_node.next = before
            before = curr_node
            curr_node = after
        return self.head

    def print_sll(self):
        l = []
        temp = self.head
        while temp is not None:
            l.append(temp.value)
            temp = temp.next
        print(l)


s_ll = S_LL()


# to append
s_ll.append(25)
s_ll.append(84)
s_ll.append(16)
s_ll.append(12)
s_ll.append(25)
s_ll.append(66)
s_ll.print_sll()
s_ll.reverse()
s_ll.print_sll()
