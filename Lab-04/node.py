'''
Author: Chase Burkdoll
KUID: 3082972
Date: 7/1/2022
Lab: lab3
Last Modified: 7/1/2022
Purpose: The node.py file contains a Node class which is the building blocks for the LinkedList data structure. 
'''


class Node:
    def __init__(self, entry):
        self.entry = entry
        self.next = None