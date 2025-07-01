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

    def preorder_dfs(self):
        result = []

        def traverse(curr_node):
            result.append(curr_node.value)
            if curr_node.left is not None:
                traverse(curr_node.left)

            if curr_node.right is not None:
                traverse(curr_node.right)

        traverse(self.root)
        return result

    def postorder_dfs(self):
        result = []

        def traverse(curr_node):
            if curr_node.left is not None:
                traverse(curr_node.left)
            if curr_node.right is not None:
                traverse(curr_node.right)
            result.append(curr_node.value)

        traverse(self.root)
        return result

    def inorder_dfs(self):
        result = []

        def traverse(curr_node):
            if curr_node.left is not None:
                traverse(curr_node.left)
            result.append(curr_node.value)
            if curr_node.right is not None:
                traverse(curr_node.right)

        traverse(self.root)
        return result


bst = BinarySearchTree()
bst.insert(50)
bst.insert(20)
bst.insert(19)
bst.insert(25)
bst.insert(55)
bst.insert(52)
bst.insert(60)

print(bst.preorder_dfs())
# print(bst.postorder_dfs())
# print(bst.inorder_dfs())
