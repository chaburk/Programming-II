from node import Node

'''
Author: Chase Burkdoll
KUID: 3082972
Date: 7/1/2022
Lab: lab3
Last Modified: 7/1/2022
Purpose: The linkedlist.py file contains a Node based implementation of the linked list data structuce, which includes functions 
to clear, insert, and remove Nodes from the list.
'''

class LinkedList:
    def __init__(self):
        self._front = None
        self._length = 0

    def clear(self):
        #Completely clears the linked list
        self._front = None
        self._length = 0

    def length(self):
        return self._length

    def get_entry(self, index):
        #Gets the value at a certain index in a linked list
        if index >= 0 and index < self._length:
            temp = self._front
            for i in range(index):
                temp = temp.next
            return temp.entry
        else:
            raise IndexError

    def set_entry(self, index, entry):
        #Will let you set an entry at any given index
        if index >= 0 and index < self._length:
            if index == 0:
                temp = self._front
                temp.entry = entry
            else:
                temp = self._front
                for i in range(index):
                    temp = temp.next
                temp.entry = entry
        else:
            raise IndexError
                

    def insert(self, index, entry):
        #Will add an entry into anywhere in the list
        if index >= 0 and index <= self._length:
            new_node = Node(entry)
            if index == 0:
                new_node.next = self._front
                self._front = new_node
            elif index == self._length:
                last_node = self._front
                for i in range(index -1):
                    last_node = last_node.next
                last_node.next = new_node
            else:
                after = self._front
                before = self._front
                for i in range(index):
                    after = after.next
                    if i < index - 1:
                        before = after
                before.next = new_node
                new_node.next = after
            self._length += 1
        else:
            raise IndexError

    def remove(self, index):
        #Will remove the node at any given index
        if index >= 0 and index < self._length and self._length > 0:
            if index == 0:
                temp = self._front 
                self._front = temp.next
                self._length -= 1
                return temp
            else:
                before = self._front
                current = self._front
                for i in range(index):
                    if i < index - 1:
                        before = before.next
                    current = current.next
                before.next = current.next
                self._length -= 1
                return current
            
        else:
            raise IndexError