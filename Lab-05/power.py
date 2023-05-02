'''
Author: Chase Burkdoll
KUID: 3082972
Date: 7/8/2022
Lab: lab5
Last Modified: 7/11/2022
Purpose: The power.py file contains a Power class that contains a single method that contains a function which 
calculates powers of numbers through recursion
'''

class Power:
    def run_power(self):
        #Method asks the user for a base and power then calls a function to calculate the value
        base = int(input("Enter a base: "))
        power = int(input("Enter an exponent: "))
        def power_func(base, power):
            #function calculates the value of a base and exponent
            while True:
                try:
                    if power >= 0: 
                        if power == 0:
                            return 1
                        elif power == 1:
                            return base
                        else:
                            return base * power_func(base, power -1)
                    else:
                        raise ValueError("Can't have a negative exponent")
                except:
                    print('Sorry, your exponent must be zero or larger')
                    power = int(input("Enter an exponent: "))
        print(power_func(base,power))
