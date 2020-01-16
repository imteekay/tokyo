from queue import Queue


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child:
            self.left_child.insert_left(value)
        else:
            self.left_child = BinaryTree(value)

    def insert_right(self, value):
        if self.right_child:
            self.right_child.insert_right(value)
        else:
            self.right_child = BinaryTree(value)

    def pre_order(self):
        print(self.value)

        if self.left_child:
            self.left_child.pre_order()

        if self.right_child:
            self.right_child.pre_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()

        if self.right_child:
            self.right_child.post_order()

        print(self.value)

    def in_order(self):
        if self.left_child:
            self.left_child.in_order()

        print(self.value)

        if self.right_child:
            self.right_child.in_order()

    def bfs(self):
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            node = queue.get()
            print(node.value)

            if node.left_child:
                queue.put(node.left_child)

            if node.right_child:
                queue.put(node.right_child)


a_node = BinaryTree('a')
a_node.insert_left('b')
a_node.insert_right('c')

b_node = a_node.left_child
b_node.insert_left('d')
b_node.insert_right('e')

c_node = a_node.right_child
c_node.insert_left('f')
c_node.insert_right('g')

d_node = b_node.left_child
e_node = b_node.right_child
f_node = c_node.left_child
g_node = c_node.right_child

a = a_node.value
b = b_node.value
c = c_node.value
d = d_node.value
e = e_node.value
f = f_node.value
g = g_node.value

print
print('---------------------------------------')
print
print("               |%s|" % (a))
print("             /     \\")
print("           |%s|     |%s|" % (b, c))
print("          /   \\    /  \\")
print("        |%s|  |%s| |%s|  |%s|" % (d, e, f, g))

# ------- Building this Tree -------
#
#                |a|
#              /     \
#            |b|     |c|
#          /   \    /   \
#       |d|   |e| |f|   |g|

print
print('---------------------------------------')
print

tree = a_node

print('Depth First: Pre Order')
print
tree.pre_order()
print

print
print('---------------------------------------')
print

print('Depth First: Post Order')
print
tree.post_order()
print

print
print('---------------------------------------')
print

print('Depth First: In Order')
print
tree.in_order()
print

print
print('---------------------------------------')
print

print('Breadth First Search')
print
tree.bfs()
print
