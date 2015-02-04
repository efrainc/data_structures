#! /usr/bin/env python
#Linked List Python file for Efrain , Mark and Henry

class Node(object):
    """Calss DocString Here"""

    def __init__(self, value, pointer = None):
        self.pointer = pointer
        self.value = value

        return None





class Linked_list(object):
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

    def __str__(self):
        output = ""
        currentposition = self.head
        while currentposition:
            # ', '.join((output, str(currentposition.value)))
            if isinstance(currentposition.value, str):
                output += "'{}'".format(currentposition.value)
            else:
                output += str(currentposition.value)
            currentposition = currentposition.pointer
            if currentposition:
                output += str(", ")

        output = "({})".format(output)
        return output

    def pop(self):
        old_head_value = self.head.value
        self.head = self.head.pointer
        return old_head_value


    def size(self):
        count = 0
        currentposition = self.head
        while currentposition:
            count += 1
            currentposition = currentposition.pointer
        return count


    def search(self, value):
        currentposition = self.head
        while currentposition:
            if currentposition.value == value:
                return currentposition
            currentposition = currentposition.pointer
        return None

    def remove(self, node):
        currentposition = self.head
        previousposition = None

        # for case when we are removing first node
        if currentposition == node:
            self.head = currentposition.pointer
            return None

        while currentposition:
            if currentposition == node:
                previousposition.pointer = currentposition.pointer
            previousposition = currentposition
            currentposition = currentposition.pointer




