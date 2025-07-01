# https://leetcode.com/problems/merge-two-binary-trees/description/


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

    # def merge_bt(self, root1, root2):
    #     if not root1:
    #         return root2
    #     if not root2:
    #         return root1

    #     root1.val += root2.val

    #     root1.left = self.merge_bt(root1.left, root2.left)
    #     root1.right = self.merge_bt(root1.right, root2.right)
    #     return root1

    def merge_bt(self, root1, root2):
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        root1.val += root2.val
        root1.left = self.merge_bt(root1.left, root2.left)
        root1.right = self.merge_bt(root1.right, root2.right)
        return root1


bt1 = BinaryTree()
bt2 = BinaryTree()
bt1.insert_from_list([1, 3, 2, 5])
bt2.insert_from_list([2, 1, 3, None, 4, None, 7])
root = bt1.merge_bt(bt1.root, bt2.root)

print(bt1.print_bin(root))
