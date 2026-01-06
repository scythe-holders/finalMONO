class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a node to the end of the circular linked list."""
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = new_node  # Points to itself
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def prepend(self, data):
        """Add a node to the beginning of the list."""
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = new_node
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        new_node.next = self.head
        current.next = new_node
        self.head = new_node

    def display(self):
        """Print the elements of the circular linked list."""
        if not self.head:
            print("List is empty")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")

    def find(self, key):
        """Search for a value in the list."""
        if not self.head:
            return False

        current = self.head
        while True:
            if current.data == key:
                return True
            current = current.next
            if current == self.head:
                break
        return False
