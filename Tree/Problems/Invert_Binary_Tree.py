# https://leetcode.com/problems/balanced-binary-tree/description/


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

    def invert_tree(self):
        def traverse(curr_node):
            if curr_node is None:
                return None
            curr_node.left, curr_node.right = curr_node.right, curr_node.left

            traverse(curr_node.left)
            traverse(curr_node.right)

        traverse(self.root)
        return self.print_tree()

    def print_tree(self):
        result = []
        queue = [self.root]
        while len(queue):
            curr_node = queue.pop(0)
            result.append(curr_node.val)
            if curr_node.left is not None:
                queue.append(curr_node.left)
            if curr_node.right is not None:
                queue.append(curr_node.right)
        return result


bt = BinaryTree()

bt.insert_from_list([4, 2, 7, 1, 3, 6, 9])

print(bt.invert_tree())
