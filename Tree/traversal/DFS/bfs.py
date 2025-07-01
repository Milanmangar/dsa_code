class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __r_insert(self, curr_node, value):
        if curr_node is None:
            return Node(value)
        if value < curr_node.value:
            curr_node.left = self.__r_insert(curr_node.left, value)

        if value > curr_node.value:
            curr_node.right = self.__r_insert(curr_node.right, value)
        return curr_node

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        self.__r_insert(self.root, value)

    def dfs(self):
        curr_node = self.root
        queue = [curr_node]
        result = []
        while len(queue) > 0:
            curr_node = queue.pop(0)
            result.append(curr_node.value)
            if curr_node.left is not None:
                queue.append(curr_node.left)
            if curr_node.right is not None:
                queue.append(curr_node.right)
        return result


bst = BinarySearchTree()
bst.insert(47)
bst.insert(21)
bst.insert(76)
bst.insert(18)
bst.insert(27)
bst.insert(52)
bst.insert(82)

print(bst.dfs())
