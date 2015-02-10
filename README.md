# data_structures
Working directory for Efrain, Mark, Henry - Python Data Structures

Linked_list
    A linked list is defined by sequence of nodes.
    Each linked list instance has a head varible which points to the
    first node in the linked list, if it exists.
    Each node is composed of a pointer and value.
    When using search function, the first node with the query value,
    is returned. If there are multiple nodes with the query value, only
    the first instance is found.

Stack
    A stack is a sequence of nodes that has a top. You can put new nodes
    on top by pushing a value to it and you can remove a node from the
    top by popping which also returns the node.

Queue
    A queue is a sequence of nodes that has a front and back. It follows
    the principle of FIFO, first in, first out. You can add new nodes to
    the end and dequeue values from the front which also removes that node.

ec_parenthetics
    Corresponding to work submitted and owned by Efrain Camacho on the
    parenthetics assignment. Captured in git hub branch ec_parenthetics.
    Funtion takes a user submitted text. Encodes it in utf-8 and evaluates
    the text for proper parentheical assignment.

Doubly-Linked-List(dll)
    A dll is a defined by a sequence of nodes each with a value and two
    pointers pointing to the next and previous nodes. It has a head and tail
    which point to the first and last nodes. Values can be added and removed
    from either the head or tail. The remove method removes the first instance
    of the value starting at the head.

    Application:
    Use a DLL if removing or adding from front and back. A DLL uses more
    memory than LL, but will be faster to remove items from end of list.
    A DLL has the functionality of a queue and a stack.
    Ex: If there is a line at the DMV, it'd better to use a DLL, because
    it is faster to remove an item from the line. This is also the case
    for a print queue, where'd we want to remove a job from the queue.


Resources:
    None

Collaborations:
    None