class Node:
    def __init__(self, data, _next, previous=None):
        self.data = data
        self.next = _next
        self.previous = previous


class LinkedList:
    def __init__(self):
        self.head = None

    def clear(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(data, None)

    def get_length(self):
        if self.head is None:
            return 0
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def find_index(self, data):
        count = 0
        if self.get_length() == 0:
            return -1
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return count
            count += 1
            current_node = current_node.next
        else:
            return -1

    def begin(self, data):
        if self.head is None:
            self.append(data)
            return

        self.head = Node(data, self.head)

    def delete(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return
        count = 0
        current_node = self.head
        while current_node:
            if count == index - 1:
                current_node.next = current_node.next.next
            current_node = current_node.next
            count += 1

    def remove_value(self, data):
        index = self.find_index(data)
        if index != -1:
            self.delete(index)

    def insert(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.begin(data)
            return
        count = 0
        current_node = self.head
        while current_node:
            if count == index - 1:
                current_node.next = Node(data, current_node.next)
                break
            current_node = current_node.next
            count += 1

    def insert_values(self, data_list):
        for data in data_list:
            self.append(data)

    def show_list(self):
        if self.head is None:
            print(None)
        current = self.head
        output = []
        while current:
            output.append(current.data)
            current = current.next

        print(output)
