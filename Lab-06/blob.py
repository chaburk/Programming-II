'''
Author: Chase Burkdoll
KUID: 3082972
Date: 7/15/2022
Lab: lab6
Last Modified: 7/20/2022
Purpose: The blob.py file contains a Blob class that takes in a 'city' / 'maze' and spreads throughout the city. It uses backtracking 
and several helper methods to spread.
'''


class Blob:
    def __init__(self, x_dim, y_dim, sewers, maze):
        self.x_dim = int(x_dim)
        self.y_dim = int(y_dim)
        self.maze = maze
        self.sewers = sewers
        self.num_people_ate = 0
        
    def mark(self, row, col):
        #Marks the location in the maze as either a sewer or a "B" for blob
        if self.maze[row][col] == "@":
            self.maze[row][col] = "@"
        else:
            self.maze[row][col] = "B"

    def is_sewer(self, row, col):
        #Checks the location in the maze to see if it is a sewer
        if self.maze[row][col] == "@":
            return True
        return False

    def is_person(self, row, col):
        #Checks the location in the maze to see if it is a person and if it is then adds to the number eaten
        if self.maze[row][col] == "P":
            self.num_people_ate += 1

    def is_valid_move(self, row, col):
        #Checks if the location in the maze is a valid square by checking the bounds
        if(row < 0) or (row >= int(self.x_dim)) or (col < 0) or (col >= int(self.y_dim)):
            return False
        if self.maze[row][col] == '#' or self.maze[row][col] == 'B':
            return False
        return True

    def spread(self, row, col):
        #Backtracking method that helps the blob spread
        self.is_person(row, col)
        self.mark(row, col)

        #Check Up
        if self.is_valid_move(row - 1, col):
            self.spread(row - 1, col)


        #Check Right
        if self.is_valid_move(row, col + 1):
            self.spread(row, col + 1)


        #Check Down
        if self.is_valid_move(row + 1, col):
            self.spread(row + 1, col)


        #Check Left
        if self.is_valid_move(row, col - 1):
            self.spread(row, col - 1)

        #Check Sewer
        if self.is_sewer(row, col):
            for sewer in self.sewers:
                self.sewers.pop(0)
                self.spread(sewer[0],sewer[1])

        return True