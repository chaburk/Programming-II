from node import Node

'''
Author: Chase Burkdoll
KUID: 3082972
Date: 6/17/2022
Lab: lab2
Last Modified: 6/22/2022
Purpose: The queue.py file contains a class that is a node implementation of a Queue.
'''

class Queue:
    def __init__(self):
        self._front = None
        self._back = None

    def is_empty(self):
        #checks if the Queue is empty
        if self._front == None:
            return True
        else:
            return False

    def enqueue(self, entry):
        #adds a node to the back of the queue
        temp = Node(entry)
        if self.is_empty():
            self._front = temp
            self._back = temp
        else:
            self._back.next = temp
            self._back = temp

    def dequeue(self):
        #removes a node from the front of the queue
        if not self.is_empty():
            temp = self._front
            self._front = temp.next
            return temp
        else:
            raise RuntimeError('Queue is empty.')

    def peek_front(self):
        #looks at the first item in the queue
        if not self.is_empty():
            return self._front.entry
        else:
            raise RuntimeError('Queue is empty.')


