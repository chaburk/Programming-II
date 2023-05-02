from tkinter.font import names
'''
Author: Chase Burkdoll
KUID: 3082972
Date: 6/10/2022
Lab: lab1
Last Modified: 6/14/2022
Purpose: The boardgame.py file contains a BoardGame class that initalizes board games objects from a user input file. With in the class there
are getter and setter functions to maintain privacy.
'''

class BoardGame:
    #class that takes in a list of strings and converts them into a BoardGame object
    def __init__(self, name, year, gb_rating, pb_rating, min_players, min_playtime):
        #construtor that creates the BoardGame objects
        self._name = name
        self._year = int(year)
        self._gb_rating = gb_rating
        self._pb_rating = pb_rating
        self._min_players = min_players
        self._min_playtime = min_playtime

    def __repr__(self):
        #String representation of the BoardGame class
        return f'{self._name} ({self._year}) [GR={self._gb_rating}, PR={self._pb_rating}, MP={self._min_players}, MT={self._min_playtime}]'

    def __lt__(self, other):
        if self._gb_rating < other._gb_rating:
            return self._gb_rating

    #A Bunch of Getter functions to maintain private variables
    def get_name(self):
        return self._name

    def get_year(self):
        return self._year

    def get_gb_rating(self):
        return self._gb_rating

    def get_pb_rating(self):
        return self._pb_rating

    def get_min_players(self):
        return self._min_players

    def get_min_playtime(self):
        return self._min_playtime

    