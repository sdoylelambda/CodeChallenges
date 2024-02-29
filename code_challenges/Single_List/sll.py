class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next_val = None


class SingleLinkedlist:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        if not self.head:
            self.head = value
        else:
            while self.head is not None:
                self.head = self.head.next_val
            self.head = value

    def print_sll(self):
        value = self.head
        while value is not None:
            print(value)
            try:
                value = value.next_val
            except:
                pass


SLL = SingleLinkedlist()
SLL.add_node(4)
SLL.print_sll()
