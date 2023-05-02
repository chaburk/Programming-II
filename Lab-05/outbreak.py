'''
Author: Chase Burkdoll
KUID: 3082972
Date: 7/8/2022
Lab: lab5
Last Modified: 7/11/2022
Purpose: The outbreak.py file contains an Outbreak class that contains a method which has a function to determine the 
number of sick people on a given day through use of recursion.
'''

class Outbreak:
    def run_outbreak(self):
        #Method asks user which day they want to know the infected count
        print('OUTBREAK!')
        day = int(input('What day do you want a sick count for?: '))
        def outbreak(day):
            #function uses recursion to determine number of sick people on given day
            while True:
                try:
                    if day > 0:
                        if day == 1:
                            return 6
                        elif day == 2:
                            return 20
                        elif day == 3:
                            return 75
                        else:
                            return outbreak(day-1) + outbreak(day-2) + outbreak(day-3)
                    else:
                        raise RuntimeError('Not a valid day')
                except:
                    print('Invalid day')
                    day = int(input('What day do you want a sick count for?: '))

        total = outbreak(day)
        print('Total people with flue:', total)
