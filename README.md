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


Hg_parenthetics
    paranthetics is a function that accepts a unicode string (text) as
    input and returns one of these three possible values:

    Return 1 if the string is "open" (there are open parens that are not 
        closed).
    Return 0 if the string is "balanced" (there are an equal number of 
        open and closed parentheses in the string).
    Return -1 if the string is "broken" (a closing parens has not been 
        proceeded by one that opens) .
    Open and closed parens must match, so "))((" would be considered "broken".
    This function utilizes the Stack datastructure. 

Resources:
    None

Collaborations:
    None