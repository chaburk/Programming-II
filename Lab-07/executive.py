from pokemon import Pokemon
from bst import BST

'''
Author: Chase Burkdoll
KUID: 3082972
Date: 7/22/2022
Lab: lab7
Last Modified: 7/28/2022
Purpose: The executive.py file contains an Executive class which takes an input file and opens it to from a list of Pokemon objects.
The class also contains a user menu that lets the user interact with the BST by creating searching for a
Pokemon, adding or removing a Pokemon, and making a copy of the BST
'''

class Executive:
    def __init__(self, file_name):
        self.file_name = file_name
        self.num_of_copies = 0

    def run(self):
        input_file = open(self.file_name + ".txt")
        pokedex = [line.split() for line in input_file]
        pokemans = [Pokemon(pokemon[0], pokemon[1], pokemon[2]) for pokemon in pokedex]

        chase_bst = BST()
        for pokemon in pokemans:
            chase_bst.add(pokemon)

        name = input('What is your name?: ')
        try:
            while True:
                print()
                print('Welcome to your Pokedex', name)
                print('what would you like to do?')
                print('1. Search through your Pokedex')
                print('2. Add to your Pokedex')
                print('3. Print your Pokedex')
                print('4. Make a copy of your Pokedex')
                print('5. Remove a Pokemon from your Pokedex')
                print('6. Quit')
                user_input = input('')
                if user_input == '1':
                    try:
                        if self.num_of_copies == 1:
                            print('1. Original')
                            print('2. Copy')
                            user_input =  input('Which BST would you like to traverse?: ')
                            if user_input == '1':
                                try:
                                    search_num = int(input('Which Pokedex ID would you like to search for?: '))
                                    print(chase_bst.search(search_num))
                                except:
                                    search_num = int(input('Which Pokedex ID would you like to search for?: '))
                                    print(chase_bst.search(search_num))
                            elif user_input == '2':
                                try:
                                    search_num = int(input('Which Pokedex ID would you like to search for?: '))
                                    print(copy.search(search_num))
                                except:
                                    search_num = int(input('Which Pokedex ID would you like to search for?: '))
                                    print(copy.search(search_num))
                        else:
                            search_num = int(input('Which Pokedex ID would you like to search for?: '))
                            print(chase_bst.search(search_num))
                    except:
                        print('Search item not found!')
                elif user_input == '2':
                    try:
                        print('ADD')
                        if self.num_of_copies == 1:
                            print('1. Original')
                            print('2. Copy')
                            user_input =  input('Which BST would you like to traverse?: ')
                            if user_input == '1':
                                us_name = input('American name of Pokemon?: ')
                                number = int(input('Pokedex number?: '))
                                jap_name = input('Japanese name of Pokemon?: ')
                                chase_bst.add(Pokemon(us_name, number, jap_name))
                            elif user_input == '2':
                                us_name = input('American name of Pokemon?: ')
                                number = int(input('Pokedex number?: '))
                                jap_name = input('Japanese name of Pokemon?: ')
                                copy.add(Pokemon(us_name, number, jap_name))
                        else:
                            us_name = input('American name of Pokemon?: ')
                            number = int(input('Pokedex number?: '))
                            jap_name = input('Japanese name of Pokemon?: ')
                            chase_bst.add(Pokemon(us_name, number, jap_name))
                    except:
                        print("Can't have duplicates!")
                elif user_input == '3':
                    print('PRINT')
                    if self.num_of_copies == 1:
                        print('1. Original')
                        print('2. Copy')
                        user_input = input('Which BST would you like to traverse?: ')
                        if user_input == '1':
                            print('1. Pre Order')
                            print('2. In Order')
                            print('3. Post Order')
                            traversal_order = input('Which traversal order would you like to do?: ')
                            if traversal_order == '1':
                            #change so it's not directly the root but for now do
                                print('PRE')
                                chase_bst.print_tree_pre(chase_bst.get_root())
                            elif traversal_order == '2':
                                print('IN')
                                chase_bst.print_tree_in(chase_bst.get_root())
                            elif traversal_order == '3':
                                print('POST')
                                chase_bst.print_tree_post(chase_bst.get_root())
                        if user_input == '2':
                            print('1. Pre Order')
                            print('2. In Order')
                            print('3. Post Order')
                            traversal_order = input('Which traversal order would you like to do?: ')
                            if traversal_order == '1':
                            #change so it's not directly the root but for now do
                                print('PRE')
                                copy.print_tree_pre(copy.get_root())
                            elif traversal_order == '2':
                                print('IN')
                                copy.print_tree_in(copy.get_root())
                            elif traversal_order == '3':
                                print('POST')
                                copy.print_tree_post(copy.get_root())
                    else:
                        print('1. Pre Order')
                        print('2. In Order')
                        print('3. Post Order')
                        traversal_order = input('Which traversal order would you like to do?: ')
                        if traversal_order == '1':
                            #change so it's not directly the root but for now do
                            print('PRE')
                            chase_bst.print_tree_pre(chase_bst.get_root())
                        elif traversal_order == '2':
                            print('IN')
                            chase_bst.print_tree_in(chase_bst.get_root())
                        elif traversal_order == '3':
                            print('POST')
                            chase_bst.print_tree_post(chase_bst.get_root())
                elif user_input == '4':
                    print('COPY')
                    if self.num_of_copies == 0:
                        copy = chase_bst.deep_copy()
                        self.num_of_copies += 1
                        print('Copy made!')
                    else:
                        print('Copy already exists!')
                elif user_input == '5':
                    print('REMOVAL')
                    try:
                        if self.num_of_copies == 1:
                            print('1. Original')
                            print('2. Copy')
                            user_input = input('Which BST would you like to remove from?: ')
                            if user_input == '1':
                                user_input = int(input('Which Pokedex index would you like to remove?: '))
                                print(chase_bst.removal(user_input))
                            if user_input == '2':
                                user_input = int(input('Which Pokedex index would you like to remove?: '))
                                print(copy.removal(user_input))
                        else:
                            user_input = int(input('Which Pokedex index would you like to remove?: '))
                            print(chase_bst.removal(user_input))

                    except:
                        print('Not in BST')
                elif user_input == '6':
                    print('QUIT')
                    print('Thank you!')
                    break
        except:
            print('something wrong')