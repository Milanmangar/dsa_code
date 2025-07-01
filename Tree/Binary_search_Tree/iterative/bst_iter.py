class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        curr_node = self.root
        while True:
            if new_node.value == curr_node.value:
                return
            elif new_node.value > curr_node.value:
                if curr_node.right is None:
                    curr_node.right = new_node
                    return
                curr_node = curr_node.right
            else:
                if curr_node.left is None:
                    curr_node.left = new_node
                    return
                curr_node = curr_node.left

    def search(self, value):
        curr_node = self.root
        while curr_node is not None:
            if curr_node.value == value:
                return True
            elif value > curr_node.value:
                curr_node = curr_node.right
            else:
                curr_node = curr_node.left
        return False


bst = BinarySearchTree()
bst.insert(40)
bst.insert(20)
bst.insert(80)
bst.insert(19)
bst.insert(23)
bst.insert(51)
bst.insert(92)
bst.insert(15)
bst.insert(98)
# print(bst.root.value)
# print(bst.root.left.value)
# print(bst.root.right.value)
# print(bst.root.right.right.right.value)

print(bst.search(16))
