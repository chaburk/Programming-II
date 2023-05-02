'''
Author: Chase Burkdoll
KUID: 3082972
Date: 6/17/2022
Lab: lab2
Last Modified: 6/22/2022
Purpose: The node.py file contains a Node class which is the building blocks for the Queue and Stack data structures. 
'''

class Node:
    def __init__(self, entry):
        self.entry = entry
        self.next = None