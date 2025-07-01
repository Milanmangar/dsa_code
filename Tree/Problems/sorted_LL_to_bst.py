# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/


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

    def print_sll(self):
        l = []
        temp = self.head
        while temp is not None:
            l.append(temp.value)
            temp = temp.next
        print(l)


s_ll = S_LL()

input1 = [-10, -3, 0, 5, 9]
for i in input1:
    # to append
    s_ll.append(i)


class Node1:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value


class bst:
    def __init__(self):
        self.root = None

    @staticmethod
    def get_mid(root):
        fast = root
        slow = root
        slow_prev = None
        while fast and fast.next:
            if fast.next.next:
                fast = fast.next.next
            else:
                fast = fast.next
            slow_prev = slow
            slow = slow.next
        return slow, slow_prev, fast

    def ll_to_bst(self, ll_root):
        def traverse(head):
            if head is None:
                return None
            if head.next is None:
                return Node1(head.value)
            mid, mid_prev, tail = self.get_mid(head)
            root = Node1(mid.value)
            mid_prev.next = None
            root.left = traverse(head)
            root.right = traverse(mid.next)
            return root

        return traverse(ll_root)

    def print_bin(self, root1):
        queue = [root1]
        result = []
        while queue:
            curr_node = queue.pop(0)
            if curr_node:
                result.append(curr_node.val)
                queue.append(curr_node.left)
                queue.append(curr_node.right)
            else:
                result.append(None)
        while result[-1] is None:
            result.pop()
        return result


bst1 = bst()
print(bst1.get_mid(s_ll.head))
root = bst1.ll_to_bst(s_ll.head)
print(bst1.print_bin(root))
