class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.is_empty():
            self.head = Node(value)
            return

        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = Node(value)

    def prepend(self, value):
        previous_head = self.head
        self.head = Node(value)
        self.head.next = previous_head

    def remove(self, value):
        if self.is_empty():
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current_node = self.head

        while current_node.next is not None:
            if current_node.value == value:
                current_node.next = current_node.next.next
                return

            current_node = current_node.next

    def search(self, value):
        found = False
        current_node = self.head

        while not found and current_node is not None:
            found = current_node.value == value
            current_node = current_node.next

        return found

    def is_empty(self):
        return self.head is None


def print_all(linked_list):
    print('All values:', end=' ')
    current_node = linked_list.head

    while current_node is not None:
        print(current_node.value, end=' ')
        current_node = current_node.next

    print()


def print_found(linked_list, value):
    found = linked_list.search(value)
    print('For value:', value, '-->', 'Found:', found, )


linked_list = LinkedList()

linked_list.remove(0)
print_all(linked_list)

linked_list.append(1)
print_all(linked_list)

linked_list.remove(0)
linked_list.remove(1)
print_all(linked_list)

linked_list.append(2)
linked_list.append(3)
print_all(linked_list)

print_found(linked_list, 1)
print_found(linked_list, 2)
print_found(linked_list, 3)

linked_list.remove(1)
print_all(linked_list)
linked_list.remove(2)
print_all(linked_list)
linked_list.remove(3)
print_all(linked_list)
