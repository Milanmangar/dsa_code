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

            # if self.length == 1:
            #     self.head.next = new_node
            #     self.tail = new_node
            #     self.length += 1
            #     return True
            # temp = self.head
            # while temp.next is not None:
            #     temp = temp.next
            # temp.next = new_node

        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = temp
        # for _ in range(self.length - 1):
        #     prev = temp
        #     temp = temp.next
        while temp.next is not None:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
            self.head = None
        return temp.value

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for i in range(self.length):
            if i == index:
                break
            temp = temp.next
        return temp

    def set(self, index, value):
        temp = self.get(index)
        if temp is None:
            return None
        else:
            temp.value = value
            return True

    def insert(self, index, value):
        new_node = Node(value)
        # if index < 0 or index > self.length:
        #     return False
        # if index == 0:
        #     return self.prepend(value)
        # if index == self.length:
        #     return self.append(value)
        # temp = self.head
        # prev = temp
        # i = 0
        # while temp.next is not None:
        #     if i == index:
        #         break
        #     prev = temp
        #     temp = temp.next
        #     i += 1
        # prev.next = new_node
        # new_node.next = temp
        # self.length += 1
        # return True
        if index < 0 or index > self.length:
            return False

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            if index == 0:
                new_node.next = self.head
                self.head = new_node
            elif index == self.length:
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp = self.head
                prev = temp
                for i in range(self.length):
                    if i == index:
                        break
                    prev = temp
                    temp = temp.next
                prev.next = new_node
                new_node.next = temp
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        # if index == 0:
        #     return self.pop_first()
        # if index == (self.length - 1):
        #     return self.pop()
        # # prev = self.get(index - 1)
        # # temp = prev.next
        # # prev.next = temp.next
        # # temp.next = None
        # temp = self.head
        # prev = temp
        # for i in range(self.length):
        #     if i == index:
        #         break
        #     prev = temp
        #     temp = temp.next
        # prev.next = temp.next
        # temp.next = None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            if index == 0:
                temp = self.head
                self.head = temp.next
                temp.next = None
            else:
                temp = self.head
                prev = temp
                for i in range(self.length):
                    if i == index:
                        break
                    prev = temp
                    temp = temp.next
                prev.next = temp.next
                temp.next = None

        self.length -= 1
        return True

    def print_sll(self):
        l = []
        temp = self.head
        while temp is not None:
            l.append(temp.value)
            temp = temp.next
        print(l)


s_ll = S_LL()

# # to append
# s_ll.append(0)
# s_ll.append(1)
# s_ll.append(2)
# s_ll.print_sll()

# # to prepend
# s_ll.prepend(0)
# s_ll.prepend(1)
# s_ll.prepend(2)
# s_ll.print_sll()

# # pop
# s_ll.append(0)
# s_ll.append(1)
# s_ll.append(2)
# s_ll.print_sll()
# print(s_ll.pop())
# print(s_ll.pop())
# print(s_ll.pop())
# print(s_ll.pop())
# s_ll.print_sll()

# # pop_first
# s_ll.append(0)
# s_ll.append(1)
# s_ll.append(2)
# s_ll.print_sll()
# print(s_ll.pop_first())
# print(s_ll.pop_first())
# print(s_ll.pop_first())
# print(s_ll.pop_first())
# s_ll.print_sll()

# # get
# s_ll.append(50)
# s_ll.append(60)
# s_ll.append(40)
# s_ll.print_sll()
# print(s_ll.get(2))
# print(s_ll.get(0))
# print(s_ll.get(3))

# # set
# s_ll.append(50)
# s_ll.append(60)
# s_ll.append(40)
# s_ll.print_sll()
# s_ll.set(2, 83)
# s_ll.set(0, 44)
# s_ll.print_sll()

# # set
# s_ll.insert(0, 83)
# s_ll.insert(1, 44)
# s_ll.insert(1, 23)
# s_ll.print_sll()
# s_ll.insert(2, 21)
# s_ll.insert(4, 97)
# s_ll.print_sll()
# s_ll.insert(0, 44)
# s_ll.print_sll()


# # remove
# s_ll.append(83)
# s_ll.append(47)
# s_ll.append(45)
# s_ll.print_sll()
# s_ll.remove(0)
# s_ll.print_sll()
# s_ll.remove(4)
# s_ll.print_sll()
# s_ll.remove(1)
# s_ll.print_sll()
