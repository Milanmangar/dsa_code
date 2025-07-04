# class Node:
#     def __init__(self, value):
#         self.left = None
#         self.right = None
#         self.value = value


# class BinarySearchTree:
#     def __init__(self):
#         self.root = None

#     def __r_insert(self, curr_node, value):
#         if curr_node is None:
#             return Node(value)
#         if value < curr_node.value:
#             curr_node.left = self.__r_insert(curr_node.left, value)

#         if value > curr_node.value:
#             curr_node.right = self.__r_insert(curr_node.right, value)
#         return curr_node

#     def insert(self, value):
#         if self.root is None:
#             self.root = Node(value)
#             return

#         self.__r_insert(self.root, value)


# bst = BinarySearchTree()
# bst.insert(40)
# bst.insert(20)
# bst.insert(50)
# bst.insert(30)
# print(bst.root.value)
# print(bst.root.left.value)
# print(bst.root.right.value)
# print(bst.root.left.right.value)

# bst.insert(20)
# print(bst.root.left.right.value)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)


##########################################################
##   Test code below will print output to "User logs"   ##
##########################################################


def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")


print("\n----- Test: Insert into an empty tree -----\n")
bst = BinarySearchTree()
print("Inserting value:", 5)
bst.r_insert(5)
check(5, bst.root.value, "Root value after inserting 5:")
check(None, bst.root.left, "Left child of root:")
check(None, bst.root.right, "Right child of root:")

print("\n----- Test: Insert values in ascending order -----\n")
bst = BinarySearchTree()
values = [1, 2, 3, 4, 5]
for val in values:
    print("Inserting value:", val)
    bst.r_insert(val)

# Check tree structure
check(1, bst.root.value, "Root value:")
check(2, bst.root.right.value, "Right child of root:")
check(3, bst.root.right.right.value, "Right child of right child of root:")
check(
    4,
    bst.root.right.right.right.value,
    "Right child's right child's right child of root:",
)
check(5, bst.root.right.right.right.right.value, "Fourth right child of root:")

print("\n----- Test: Insert values in descending order -----\n")
bst = BinarySearchTree()
values = [5, 4, 3, 2, 1]
for val in values:
    print("Inserting value:", val)
    bst.r_insert(val)

# Check tree structure
check(5, bst.root.value, "Root value:")
check(4, bst.root.left.value, "Left child of root:")
check(3, bst.root.left.left.value, "Left child of left child of root:")
check(2, bst.root.left.left.left.value, "Left child's left child's left child of root:")
check(1, bst.root.left.left.left.left.value, "Fourth left child of root:")

print("\n----- Test: Insert values in mixed order -----\n")
bst = BinarySearchTree()
values = [3, 1, 4, 5, 2]
for val in values:
    print("Inserting value:", val)
    bst.r_insert(val)

# Check tree structure
check(3, bst.root.value, "Root value:")
check(1, bst.root.left.value, "Left child of root:")
check(2, bst.root.left.right.value, "Right child of left child of root:")
check(4, bst.root.right.value, "Right child of root:")
check(5, bst.root.right.right.value, "Right child of right child of root:")

print("\n----- Test: Insert duplicate values -----\n")
bst = BinarySearchTree()
values = [3, 3, 3]
for val in values:
    print("Inserting value:", val)
    bst.r_insert(val)

# Check tree structure
check(3, bst.root.value, "Root value:")
check(None, bst.root.left, "Left child of root:")
check(None, bst.root.right, "Right child of root:")
