# https://leetcode.com/problems/validate-binary-search-tree/description/


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

    # def valid_bst(self, root):
    #     def traverse(node):
    #         if node is None:
    #             return None
    #         left = traverse(node.left)
    #         right = traverse(node.right)
    #         if left is not None:
    #             if left is False or left.val >= node.val:
    #                 return False
    #         if right is not None:
    #             if right is False or right.val <= node.val:
    #                 return False
    #         return node

    #     return False if traverse(root) is False else True

    def valid_bst(self, root):
        def traverse(node, min_val, max_val):
            if node is None:
                return True
            if node.val <= min_val or node.val >= max_val:
                return False
            left = traverse(node.left, min_val, node.val)
            right = traverse(node.right, node.val, max_val)
            return left & right

        return traverse(root, float("-inf"), float("inf"))


bt1 = BinaryTree()
bt1.insert_from_list(
    [10, 5, 15, 3, 7, 12, 18, None, None, None, None, None, None, None, None]
)
print(bt1.print_bin(bt1.root))
print(bt1.valid_bst(bt1.root))
