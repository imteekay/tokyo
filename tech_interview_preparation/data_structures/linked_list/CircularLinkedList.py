class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.head.next = self.head
            return

        current_node = self.head

        while current_node.next is not self.head:
            current_node = current_node.next

        current_node.next = Node(value, self.head)

    def prepend(self, value):
        pass

    def remove(self, value):
        pass

    def is_empty(self):
        return self.head is None

    def search(self, value):
        pass

    def size(self):
        pass


def print_all(linked_list):
    print('All values:', end=' ')
    current_node = linked_list.head

    while current_node.next is not linked_list.head:
        print(current_node.value, end=' ')
        current_node = current_node.next

    print(current_node.value, end=' ')
    print()


linked_list = CircularLinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
print_all(linked_list)
