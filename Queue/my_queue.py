from node import Node

class Queue:
    def __init__(self):
        self.head = self.tail = None
    
    def __repr__(self) -> str:
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next

        nodes.reverse()
        return str(nodes)


    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.tail = self.head = new_node
        
        else:
            self.tail.next = new_node
            self.tail = new_node


    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')

        first_node = self.head
        self.head = first_node.next
        first_node.next = None

        if self.head is None:
            self.tail = None

        return first_node.data

    def peek(self):
        if self.is_empty():
            raise Exception('Queue is empty')

        return self.head.data
    
    def is_empty(self):
        return self.tail == None

    def size(self):
        count = 0
        node = self.head

        while node is not None:
            count += 1
            node = node.next

        return count

    def clear(self):
        current_node = self.head

        while current_node is not None:
            next_node = current_node.next
            del current_node.data
            del current_node.next
            del current_node
            current_node = next_node
        
        self.head = self.tail = None