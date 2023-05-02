from boardgame import BoardGame
'''
Author: Chase Burkdoll
KUID: 3082972
Date: 6/10/2022
Lab: lab1
Last Modified: 6/14/2022
Purpose: The executive.py file contains an Executive class takes in a input file from the user, and uses the content from the file to create a list of BoardGame objects.
After, the user is prompted with a user menu to interact with the objects through set functions.
'''
class Executive:
    def __init__(self, file_name):
        self._file_name = file_name

    def run(self):
        #Opens the file and creates a list of boardgame objects
        board_objects = [] 
        input_file = open(str(self._file_name) + '.txt')
        for line in input_file:
            new_game = line.split()
            game = BoardGame(new_game[0], new_game[1], new_game[2], new_game[3], new_game[4], new_game[5])
            board_objects.append(game)
            
        #Prints the user Menu and the main while loop 
        print("Welcome to John Gibbon's board game collection")
        print('User Menu')
        print('-----------------------------')
        while True:
            print('1. Get a list of board game scores from highest to lowest')
            print('2. Get games from a certain year')
            print('3. Get games within a certain ranking')
            print("4. Get the difference between Dr. Gibbons rating and the People's rating")
            print('5. Get a game with a min playtime or less')
            print('6. QUIT')
            user_input = int(input('What would you like to do(1-6): '))
            if user_input == 1:
                now_sorted = sorted(board_objects, reverse = True)
                for games in now_sorted:
                    print(games)
            elif user_input == 2:
                user_input = input("What year do you want? ")
                for games in board_objects:
                    if int(user_input) == games.get_year():
                        print(games)
            elif user_input == 3:
                user_input = input("Select lower ranking range: ")
                user_input2 = input("Select higher ranking range: ")
                for games in board_objects:
                    if games.get_gb_rating() >= user_input and games.get_gb_rating() <= user_input2:
                        print(games)
            elif user_input == 4:
                user_input = float(input('Enter a number to see where the people and Dr. Gibbons differ on rating: (0-10): '))
                for games in board_objects:
                    #add a round here
                    if abs(float(games.get_gb_rating()) - float(games.get_pb_rating())) >= user_input:
                        print(games)
            elif user_input == 5:
                user_input = int(input('Enter a playtime: '))
                for games in board_objects:
                    if int(games.get_min_playtime()) <= user_input:
                        print(games)
            elif user_input == 6:
                print('Thank you for hanging')
                break
            else:
                print('Please input a valid choice')