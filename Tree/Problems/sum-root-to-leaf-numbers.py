# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value


class BinaryTree:
    def __init__(self):
        self.root = None  # The root of the tree

    def insert_from_list(self, values):
        # Inserts nodes based on the list representation
        if not values:
            return None
        self.root = Node(values[0])  # The first value is the root
        queue = [self.root]
        index = 1  # Start from the second element in the list

        while index < len(values):
            current_node = queue.pop(0)  # Get the current node from the queue

            # Check if the current node should have a left child
            if values[index] is not None:
                current_node.left = Node(values[index])
                queue.append(current_node.left)  # Add the left child to the queue
            index += 1

            # Check if the current node should have a right child
            if index < len(values) and values[index] is not None:
                current_node.right = Node(values[index])
                queue.append(current_node.right)  # Add the right child to the queue
            index += 1

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

    def sum_bt(self, root):
        def traverse(node, val):
            if node is None:
                return 0
            curr_val = node.val + val * 10
            if node.left is None and node.right is None:
                return curr_val
            return traverse(node.left, curr_val) + traverse(node.right, curr_val)

        return traverse(root, 0)


bt1 = BinaryTree()
bt1.insert_from_list([4, 9, 0, 5, 1])

print(bt1.sum_bt(bt1.root))
