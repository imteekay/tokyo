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
        if self.is_empty():
            self.head = Node(value)
            self.head.next = self.head
            return

        current_node = self.head

        while current_node.next is not self.head:
            current_node = current_node.next

        self.head = Node(value, self.head)
        current_node.next = self.head

    def remove(self, value):
        if self.is_empty():
            return

        if self.head.value == value:
            if self.head == self.head.next:
                self.head = None
                return

            current_node = self.head

            while current_node.next is not self.head:
                current_node = current_node.next

            self.head = self.head.next
            current_node.next = self.head

        current_node = self.head

        while current_node.next is not self.head:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                return

            current_node = current_node.next

    def is_empty(self):
        return self.head is None

    def search(self, value):
        if self.is_empty():
            return False

        if self.head.value == value:
            return True

        found = False
        current_node = self.head

        while not found and current_node.next is not self.head:
            found = current_node.next.value == value
            current_node = current_node.next

        return found

    def size(self):
        list_length = 0

        if self.is_empty():
            return list_length

        current_node = self.head

        while current_node.next is not self.head:
            list_length += 1
            current_node = current_node.next

        return list_length + 1


def print_all(linked_list):
    if linked_list.is_empty():
        print('Empty!')
        return

    print('All values:', end=' ')
    current_node = linked_list.head

    while current_node.next is not linked_list.head:
        print(current_node.value, end=' ')
        current_node = current_node.next

    print(current_node.value, end=' ')
    print()


def print_found(linked_list, value):
    found = linked_list.search(value)
    print('For value:', value, '-->', 'Found:', found, )


def print_size(linked_list):
    list_length = linked_list.size()
    print('Size:', list_length)


linked_list = CircularLinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
print_all(linked_list)  # 1 2 3
print_size(linked_list)  # 3
print_found(linked_list, 0)  # False
print_found(linked_list, 1)  # True
print_found(linked_list, 2)  # True
print_found(linked_list, 3)  # True
print_found(linked_list, 4)  # False

linked_list.prepend(0)
linked_list.prepend(-1)

print_all(linked_list)  # -1 0 1 2 3
print_size(linked_list)  # 5

linked_list.remove(-1)
print_all(linked_list)  # 0 1 2 3

linked_list.remove(0)
print_all(linked_list)  # 1 2 3

linked_list.remove(1)
print_all(linked_list)  # 2 3

linked_list.remove(2)
print_all(linked_list)  # 3

linked_list.remove(3)

print_all(linked_list)  # empty
print_size(linked_list)  # 0
