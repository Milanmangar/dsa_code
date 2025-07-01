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

    # def good_nodes(self):

    # def traverse(curr_node):
    #     if curr_node is None:
    #         return 0, curr_node
    #     left_good_node_count, after_node = traverse(curr_node.left)
    #     if after_node is not None and curr_node.value <= after_node.value:
    #         return left_good_node_count + 1, curr_node
    #     right_good_node_count, after_node = traverse(curr_node.right)
    #     if after_node is not None and curr_node.value <= after_node.value:
    #         return right_good_node_count + 1, curr_node
    #     return left_good_node_count + right_good_node_count, curr_node

    # def traverse(curr_node):
    #     if curr_node is None:
    #         return 0
    #     left_good_node_count = traverse(curr_node.left)
    #     right_good_node_count = traverse(curr_node.right)
    #     if curr_node.left is not None and curr_node.left.value >= curr_node.value:
    #         left_good_node_count += 1
    #     if curr_node.right is not None and curr_node.right.value >= curr_node.value:
    #         right_good_node_count += 1
    #     return left_good_node_count + right_good_node_count

    # return traverse(self.root) + 1
    # node_stack_list = []

    # def traverse(curr_node):
    #     if curr_node is None:
    #         return 0
    #     node_stack_list.append(curr_node.value)
    #     left_good_node_count = traverse(curr_node.left)
    #     right_good_node_count = traverse(curr_node.right)
    #     if max(node_stack_list, default=0) == node_stack_list.pop():
    #         return left_good_node_count + right_good_node_count + 1

    #     return left_good_node_count + right_good_node_count

    # def traverse(curr_node, node_value):
    #     if curr_node is None:
    #         return 0
    #     left_good_node_count = traverse(
    #         curr_node.left, max(curr_node.value, node_value)
    #     )
    #     right_good_node_count = traverse(
    #         curr_node.right, max(curr_node.value, node_value)
    #     )
    #     if curr_node.value >= node_value:
    #         return left_good_node_count + right_good_node_count + 1

    #     return left_good_node_count + right_good_node_count

    # return traverse(self.root, self.root.value)

    def good_nodes(self) -> int:
        def traverse(curr_node, node_value):
            if curr_node is None:
                return 0
            res = 1 if curr_node.val >= node_value else 0
            res += traverse(curr_node.left, max(curr_node.val, node_value))
            res += traverse(curr_node.right, max(curr_node.val, node_value))

            return res

        return traverse(self.root, self.root.val)


bt = BinaryTree()

bt.insert_from_list([3, 1, 4, 3, None, 1, 5])

print(bt.good_nodes())
