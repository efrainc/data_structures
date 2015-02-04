#Linked List Python file for Efrain , Mark and Henry

class Node(object):
    """Calss DocString Here"""

    def __init__(self, value, pointer = None):
        self.pointer = pointer
        self.value = value

        return None





class linked_list(object):
    """" """

    def __init__(self):
        self.head = None

    def insert(self, value):

        if self.head == None:
            self.head = Node(value)
        else:
            new_node = Node(value, self.head)
            self.head = new_node

        print self.head


