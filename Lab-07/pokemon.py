'''
Author: Chase Burkdoll
KUID: 3082972
Date: 7/22/2022
Lab: lab7
Last Modified: 7/24/2022
Purpose: the pokemon.py file contains a Pokemon class that initalizes a Pokemon with an American name, 
pokedex number, and a Japanese name. The Pokemon class also overloads default comparison operators to compare objects.
'''

class Pokemon:
    def __init__(self, us_name, dex_num, jap_name):
        #Initalizes a Pokemon with an American name, pokedex number, and a Japanese name
        self.us_name = us_name
        self.dex_num = int(dex_num)
        self.jap_name = jap_name

    def __lt__(self, other):
        #Compares Pokemon object to other Pokemon objects as well as Pokemon objects to numbers using the less than operater
        if isinstance(other, int):
            return self.dex_num < other
        else:
            return self.dex_num < other.dex_num

    def __gt__(self, other):
        #Compares Pokemon object to other Pokemon objects as well as Pokemon objects to numbers using the greater than operater
        if isinstance(other, int):
            return self.dex_num > other
        else:
            return self.dex_num > other.dex_num

    def __eq__(self, other):
        #Compares Pokemon object to other Pokemon objects as well as Pokemon objects to numbers using the equal to operater
        if isinstance(other, int):
            return self.dex_num == other
        else:
            return self.dex_num == other.dex_num

    def __repr__(self):
        return f'US = {self.us_name} / Jap = {self.jap_name} #{self.dex_num}'
            