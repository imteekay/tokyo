class Node:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root:
            self.insert_node(self.root, value)
        else:
            self.root = Node(value)

    def insert_node(self, current_node, value):
        if current_node.value <= value and current_node.left_node:
            self.insert_node(current_node.left_node, value)
        elif value <= current_node.value:
            current_node.left_node = Node(value)
        elif current_node.right_node:
            self.insert_node(current_node.right_node, value)
        else:
            current_node.right_node = Node(value)


bst = BinarySearchTree()

bst.insert(15)
bst.insert(10)
bst.insert(8)
bst.insert(12)
bst.insert(20)
bst.insert(17)
bst.insert(25)
bst.insert(19)

# print('Find 15')
# print(bst.find(15))
# print('Find 10')
# print(bst.find(10))
# print('Find 8')
# print(bst.find(8))
# print('Find 12')
# print(bst.find(12))
# print('Find 20')
# print(bst.find(20))
# print('Find 17')
# print(bst.find(17))
# print('Find 25')
# print(bst.find(25))
# print('Find 19')
# print(bst.find(19))
# print('Find 0')
# print(bst.find(0))

# print()

# print('Pre Order')
# bst.pre_order()
# print()

# print('In Order')
# bst.in_order()
# print()

# print('Post Order')
# bst.post_order()
# print()

# print('BFS')
# bst.bfs()
