from node import Node

class Stack:
    def __init__(self):
        self.top = None
    
    def __repr__(self) -> str:
        node = self.top
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next

        return str(nodes[::-1])

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
    
    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')

        last_node = self.top
        self.top = last_node.next

        return last_node.data

    def peek(self):
        if self.is_empty():
            raise Exception('Queue is empty')

        return self.top.data
    
    def is_empty(self):
        return self.top == None

    def size(self):
        count = 0
        node = self.top

        while node is not None:
            count += 1
            node = node.next

        return count

    def clear(self):
        current_node = self.top

        while current_node is not None:
            next_node = current_node.next
            del current_node.data
            del current_node.next
            del current_node
            current_node = next_node
        
        self.top = None