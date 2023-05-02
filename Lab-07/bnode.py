'''
Author: Chase Burkdoll
KUID: 3082972
Date: 7/22/2022
Lab: lab7
Last Modified: 7/24/2022
Purpose: the bnode.py file contains a BNode class which contains an entry, a left, and a right variables to 
help construct the BST data structure.
'''

class BNode:
    def __init__(self, entry):
        #intializes an entry and two variables which point to None
        self.entry = entry
        self.left = None
        self.right = None