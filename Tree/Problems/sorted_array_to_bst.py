# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value


class bst:
    def __init__(self):
        self.root = None

    def arr_to_bst(self, arr):
        def traverse(left, right):
            if left > right:
                return None
            mid = (right + left) // 2
            root = Node(arr[mid])
            root.left = traverse(left, mid - 1)
            root.right = traverse(mid + 1, right)
            return root

        self.root = traverse(0, len(arr) - 1)

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
bst1.arr_to_bst([-10, -3, 0, 5, 9])
bst1.print_bin(bst1.root)
