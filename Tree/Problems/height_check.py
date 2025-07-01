# https://leetcode.com/problems/balanced-binary-tree/description/


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


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

    # def preorder_dfs(self):

    #     def traverse(curr_node, height=0, curr_result=True):
    #         if curr_node.left is not None:
    #             height += 1
    #             if height > 2:
    #                 return False
    #             curr_result = traverse(curr_node.left, height)
    #         if curr_result is False:
    #             return curr_result

    #         # while back tracking from parent node, if there was left node
    #         # subtracting by 1 so that going to right node, it will have height
    #         # upto parent node
    #         if curr_node.left is not None:
    #             height -= 1

    #         if curr_node.right is not None:
    #             height += 1
    #             if height > 2:
    #                 return False
    #             curr_result = traverse(curr_node.right, height)
    #         if curr_result is False:
    #             return curr_result
    #         return curr_result

    #     return traverse(self.root)

    def difference_less_than_one_1(self):
        def traverse(curr_node):
            # Base case: If the node is None, the depth is 0
            if curr_node is None:
                return 0
            # Recursively find the depth of the left and right subtrees
            left_depth = traverse(curr_node.left)
            right_depth = traverse(curr_node.right)
            if (
                right_depth is False
                or left_depth is False
                or abs(left_depth - right_depth) > 1
            ):
                return False
            # Return the greater of the two depths plus 1 for the current node
            return max(left_depth, right_depth) + 1

        # Helper method to calculate the max depth
        result = True
        if traverse(self.root) is False:
            result = False
        return result

    def difference_less_than_one_2(self):
        def traverse(curr_node):
            # Base case: If the node is None, the depth is 0
            if curr_node is None:
                return [True, 0]
            # Recursively find the depth of the left and right subtrees
            left_depth = traverse(curr_node.left)
            right_depth = traverse(curr_node.right)
            # will be False first time when abs(left_depth[1] - right_depth[1]) > 1 and
            # backtracing result will be true or false according to result from child node
            is_balanced = (
                right_depth[0] is True
                and left_depth[0] is True
                and abs(left_depth[1] - right_depth[1]) <= 1
            )
            # Return the greater of the two depths plus 1 for the current node
            return [is_balanced, max(left_depth[1], right_depth[1]) + 1]

        return traverse(self.root)


bt = BinaryTree()
# bt.insert_from_list([1, 14, 12, 2, 3, 18, 15, 26])
# bt.insert_from_list([1, None, 2, None, 3])
# bt.insert_from_list([1, 2, 3, None, None, 4, None, 5])

bt.insert_from_list([3, 9, 20, None, None, 15, 7])

print(bt.difference_less_than_one_2())
