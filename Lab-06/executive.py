from tracemalloc import start
from blob import Blob

'''
Author: Chase Burkdoll
KUID: 3082972
Date: 7/15/2022
Lab: lab6
Last Modified: 7/20/2022
Purpose: The executive.py file contains a run method that takes in an input file and splits the information up to create an Blob object
After the create of the blob object, run will display the results.
'''

class Executive:
    def __init__(self, file_name):
        self.file_name = file_name

    def run(self):
        try:
            try:
                input_file = open(self.file_name + '.txt')
            except:
                print('Wrong name of input file')
            maze = [line.split() for line in input_file]
            dimensions = maze.pop(0)
            starting_cord = maze.pop(0)
            if int(dimensions[0]) < 1 or int(dimensions[1]) < 1:
                raise RuntimeError
            if int(starting_cord[0]) > int(dimensions[0]) or int(starting_cord[0]) < 0 or int(starting_cord[1]) < 0 or int(starting_cord[1]) > int(dimensions[1]):
                raise RuntimeError
            sewers = [] 
            new_maze = []
            for line in maze:
                for i in line:
                    new_maze.append(list(i))

            for i in range(int(dimensions[0])):
                for j in range(int(dimensions[1])):
                    if new_maze[i][j] == '@':
                        sewers.append([i,j])

            #Blob object creation             
            blob = Blob(dimensions[0], dimensions[1], sewers, new_maze)

            #Calling the blob object
            blob.spread(int(starting_cord[0]), int(starting_cord[1]))
            
            #Results of the blob spreading
            for line in blob.maze:
                print()
                for symbol in line:
                    print(symbol, end=" ")
            print()
            #Number of people consumed in the blob spread
            print('Total eaten:', blob.num_people_ate)
        except:
            print('something wrong with input')

    

