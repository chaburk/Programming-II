from node import Node

'''
Author: Chase Burkdoll
KUID: 3082972
Date: 6/17/2022
Lab: lab2
Last Modified: 6/22/2022
Purpose: The stack.py file contains a class that is a node implementation of a Stack.
'''

class Stack:
    def __init__(self):
        self._top = None
    
    def push(self, entry):
        #Puts a node of the top of the stack
        temp = Node(entry)
        temp.next = self._top
        self._top = temp

    def pop(self):
        #Takes a node off the top of the stack
        if not self.is_empty():
            temp = self._top
            self._top = temp.next
            return temp.entry
        else:
            raise RuntimeError('Nothing in the stack.')
    
    def is_empty(self):
        #checks if the Stack is empty
        if self._top == None:
            return True
        else:
            return False

    def peek(self):
        #If there is an item on the stack it returns the entry from the top node
        if not self.is_empty():
            return self._top.entry
        else:
            raise RuntimeError('Nothing in the stack.')

