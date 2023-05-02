from traceback import print_tb
from browser import Browser

'''
Author: Chase Burkdoll
KUID: 3082972
Date: 6/24/2022
Lab: lab3
Last Modified: 6/25/2022
Purpose: The executive.py file contains a class that takes in a file_name and a run method that opens the input file and
splits it into a list of commands. After spliting the file into commands, the method iterates through the list and it sends the command to
a Browser class to handle the commands. 
'''


class Executive:
    def __init__(self, file_name):
        self._file_name = file_name

    def run(self):
        #Takes in the user input file and breaks into commands to ran
        input_file = open(self._file_name + '.txt')
        commands = [line.split() for line in input_file]
        browser = Browser()
        for command in commands:
            try:
                if command[0] == 'NAVIGATE':
                    browser.navigate_to(command[1])
                elif command[0] == 'FORWARD':
                    browser.forward()
                elif command[0] == 'BACK':
                    browser.back()
                elif command[0] == 'HISTORY':
                    browser.history()
            except:
                print('Invalid Input')
            


    
        

    
