class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert_after(self, target_data, data):
        new_node = Node(data)
        current = self.head
        while current is not None:
            if current.data == target_data:
                if current.next is not None:
                    new_node.next = current.next
                    current.next.prev = new_node
                current.next = new_node
                new_node.prev = current
                break
            current = current.next

    def insert_before(self, target_data, data):
        new_node = Node(data)
        current = self.head
        while current is not None:
            if current.data == target_data:
                if current.prev is not None:
                    new_node.prev = current.prev
                    current.prev.next = new_node
                current.prev = new_node
                new_node.next = current
                if current == self.head:
                    self.head = new_node
                break
            current = current.next

    def delete(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                break
            current = current.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.prepend(3)
ll.insert_before(1, 4)
ll.insert_after(3, 5)
ll.delete(1)
ll.display()