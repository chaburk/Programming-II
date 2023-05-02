from stack import Stack

'''
Author: Chase Burkdoll
KUID: 3082972
Date: 6/17/2022
Lab: lab2
Last Modified: 6/22/2022
Purpose: the process.py file contains a class that contains a stack to help the cpu_scheduler run.
'''

class Process:
    def __init__(self, name):
        self._name = name
        self._stack = Stack()

    def add_to_stack(self, entry):
        #pushes the call onto the Process's stack and then returns the top item
        self._stack.push(entry)
        return self._stack.peek()

    def get_name(self):
        return self._name

    def get_stack(self):
        return self._stack


    