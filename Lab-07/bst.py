from bnode import BNode
from pokemon import Pokemon

'''
Author: Chase Burkdoll
KUID: 3082972
Date: 7/22/2022
Lab: lab7
Last Modified: 7/28/2022
Purpose: bst.py contains a BST class which contains methods to search, add, remove, copy, and print traversal orders for 
a Binary Search Tree
'''

class BST:
    def __init__(self):
        self._root = None

    def search(self, search_key):
        #Method calls a recursive method _rec_search
        return self._rec_search(search_key, self._root)

    def _rec_search(self, search_key, cur_node):
        #Method traverses the BST to see if a certain key is in the tree and returns the object
        if cur_node == None:
            raise RuntimeError
        if cur_node.entry < search_key:
            return self._rec_search(search_key, cur_node.right)
        if cur_node.entry > search_key:
            return self._rec_search(search_key, cur_node.left)
        if cur_node.entry == search_key:
            return f'{cur_node.entry.us_name} / {cur_node.entry.jap_name} (pokedex #{cur_node.entry.dex_num}) is in the list!'

    def add(self, entry):
        #Method that calls a recursive add method or if empty adds the root
        if self._root == None:
            self._root = BNode(entry)
        else:
            self._rec_add(entry, self._root)

    def _rec_add(self, entry, cur_node):
        #inserts the entries in a Node and then adds to the BST based on overloading magic methods
        if cur_node.entry == entry:
            raise RuntimeError
        if cur_node.entry < entry:
            if cur_node.right == None:
                cur_node.right = BNode(entry)
            else:
                self._rec_add(entry, cur_node.right)
        if cur_node.entry > entry:
            if cur_node.left == None:
                cur_node.left = BNode(entry)
            else:
                self._rec_add(entry, cur_node.left)
    
    def removal(self, remove_key):
        #Method that calls a recursive removal method
        if self._root == None:
            print('BST is empty')
            raise RuntimeError('BST is empty!')
        else:
            return self._rec_removal(remove_key, self._root)

    def _rec_removal(self, remove_key, cur_node):
        #Method that removes a certain node based on the remove_key and then adjusts the tree
        if cur_node.entry == remove_key:
            if remove_key == self._root.entry:
                temp = self._root
                replace_value = self._find_replacement_value(self._root.left)
                self.removal(replace_value.entry)
                self._root = replace_value
                self._root.left = temp.left
                self._root.right = temp.right
                return f'{cur_node.entry} was removed from the list!'
            return cur_node
        if cur_node.entry < remove_key:
            found = self._rec_removal(remove_key, cur_node.right)
            if isinstance(found, BNode):
                if found.entry == remove_key and found.left == None and found.right == None:
                    cur_node.right = None
                    return f'{found.entry} was removed from the list!'
                elif found.entry == remove_key and found.left == None:
                    cur_node.right = found.right
                    return f'{found.entry} was removed from the list!'
                elif found.entry == remove_key and found.right == None:
                    cur_node.right = found.left
                    return f'{found.entry} was removed from the list!'
                else:
                    replacement_child = self._find_replacement_value(found.left)
                    self.removal(replacement_child.entry)
                    cur_node.right = replacement_child
                    replacement_child.left = found.left
                    replacement_child.right = found.right
                    return f'{found.entry} was removed from the tree'
            else:
                return found

        if cur_node.entry > remove_key:
            found = self._rec_removal(remove_key, cur_node.left)
            if isinstance(found, BNode):
                if found.entry == remove_key and found.left == None and found.right == None:
                    cur_node.left = None
                    return f'{found.entry} was removed from the list!'
                elif found.entry == remove_key and found.left == None:
                    cur_node.left = found.right
                    return f'{found.entry} was removed from the list!'
                elif found.entry == remove_key and found.right == None:
                    cur_node.left = found.left
                    return f'{found.entry} was removed from the list!'
                else:
                    replacement_child = self._find_replacement_value(found.left)
                    self.removal(replacement_child.entry)
                    cur_node.left = replacement_child
                    replacement_child.left = found.left
                    replacement_child.right = found.right
                    return f'{found.entry} was removed from the tree'
            else:
                return found

    def print_tree_pre(self, cur_node):
        #Method prints the BST in a pre traversal order
        print(cur_node.entry)
        if cur_node.left != None:
            self.print_tree_pre(cur_node.left)
        if cur_node.right != None:
            self.print_tree_pre(cur_node.right)
        return

    def print_tree_in(self, cur_node):
        #Method prints the BST in a in traversal order
        if cur_node.left != None:
            self.print_tree_in(cur_node.left)
        print(cur_node.entry)
        if cur_node.right != None:
            self.print_tree_in(cur_node.right)
        return

    def print_tree_post(self, cur_node):
        #Method prints the BST in a post traversal order
        if cur_node.left != None:
            self.print_tree_post(cur_node.left)
        if cur_node.right != None:
            self.print_tree_post(cur_node.right)
        print(cur_node.entry)
        return
    
    def _find_replacement_value(self, cur_node):
        #Helper method that finds the right most node
        if cur_node.right != None:
            return self._find_replacement_value(cur_node.right)
        if cur_node.right == None:
            return cur_node

    def deep_copy(self):
        #Method that calls a recursive method to create a copy
        if self._root != None:
            new_bst = BST()
            return self._rec_deep_copy(new_bst, self._root)
        else:
            raise RuntimeError

    def _rec_deep_copy(self, bst, cur_node):
        #Method traverses the BST in an pre-order traversal and creates a copy BST
        if cur_node != None:
            bst.add(cur_node.entry)
            self._rec_deep_copy(bst, cur_node.left)
            self._rec_deep_copy(bst, cur_node.right)
        return bst

    def get_root(self):
        #Getter function to get self._root
        return self._root



