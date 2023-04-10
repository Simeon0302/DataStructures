from node import Node

class LinkedList:
    def __init__(self, nodes=None) -> None:
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for el in nodes:
                node.next = Node(data=el)
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return str(nodes)
    
    def add_first(self, data):
        node = Node(data=data)
        node.next = self.head
        self.head = node

    def add_last(self, data):
        node = Node(data=data)
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node_data):
        if self.head is None:
            raise Exception('This list is empty')
        for node in self:
            if node.data == target_node_data:
                new_node = Node(data=new_node_data)
                new_node.next = node.next
                node.next = new_node
                return
            node = node.next

        raise Exception('Cannot find node with data %s' % target_node_data)
    
    def add_before(self, target_node_data, new_node_data):
        if self.head is None:
            raise Exception('This list is empty')
        
        new_node = Node(data=new_node_data)
        if self.head.data == target_node_data:
            new_node.next = self.head
            self.head = new_node
        
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
        
        raise Exception('Cannot find node with data %s' % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception('List is empty')
        
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                return
            prev_node = node
        
        raise Exception('Cannot find node with data %s' % target_node_data)

    def get(self, index):
        if self.head is None:
            raise Exception('List is empty')
        
        current_index = 0
        for node in self:
            if current_index == index:
                return node
            current_index += 1
        
        raise IndexError('Index %d is out of range' % index)

    def reverse(self):
        prev_node = None
        current_node = self.head
        next_node = None

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def clear(self):
        current_node = self.head

        while current_node is not None:
            next_node = current_node.next
            del current_node.data
            del current_node.next
            del current_node
            current_node = next_node
        
        self.head = None