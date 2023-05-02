from outbreak import Outbreak
from power import Power
from fibonacci import Fibonacci

'''
Author: Chase Burkdoll
KUID: 3082972
Date: 7/8/2022
Lab: lab5
Last Modified: 7/11/2022
Purpose: The executive.py file contains a user menu and three class objects that run methods based on user input
'''

class Executive:
    def run(self):
        #Method has a user menu to call object methods
        outbreak_ob = Outbreak()
        power_ob = Power()
        fib_ob = Fibonacci()
        power = True
        while power:
            try:
                print('Which program do you want to run?: ')
                print('1. Power')
                print('2. Outbreak')
                print('3. Fibonacci')
                print('4. QUIT')
                user_input = int(input('> '))
                if user_input == 1:
                    power_ob.run_power()
                elif user_input == 2:
                    outbreak_ob.run_outbreak()
                elif user_input == 3:
                    print(fib_ob.run_fib())
                elif user_input == 4:
                    print('Thank you for running!')
                    power = False
                else:
                    raise ValueError('Invalid input')
            except:
                print('Not a valid choice')
                print('Which program do you want to run?: ')
                print('1. Power')
                print('2. Outbreak')
                print('3. Fibonacci')
                print('4. QUIT')
                user_input = int(input('> '))
