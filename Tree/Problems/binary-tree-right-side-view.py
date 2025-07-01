# https://leetcode.com/problems/validate-binary-search-tree/description/


import collections


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

    def dfs(self, root):
        nodes = collections.deque([root])
        result = []
        while nodes:
            right_side = None
            for _ in range(len(nodes)):
                node = nodes.popleft()
                if node:
                    right_side = node.val
                    nodes.append(node.left)
                    nodes.append(node.right)
            if right_side is not None:
                result.append(right_side)

        return result


bt1 = BinaryTree()
bt1.insert_from_list([0, 1, 2, None, 3, 4, None, None, 5, 9, None, None, 6, 10, None])
print(bt1.print_bin(bt1.root))
print(bt1.dfs(bt1.root))
