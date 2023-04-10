class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return str(self.data)