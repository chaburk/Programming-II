'''
Author: Chase Burkdoll
KUID: 3082972
Date: 7/8/2022
Lab: lab5
Last Modified: 7/11/2022
Purpose: The fibonacci.py file contains an Fibonacci class that contains a method which has a function to determine the fibonacci number
at a certain value/index and the ability to see if a number is in the fibonacci sequence.
'''

class Fibonacci:
    def run_fib(self):
        #Method that asks for a mode and value then either determines the fibonacci number at that value/index 
        #or check if the value is in the fibonacci sequence
        mode = input('input mode (i, v): ')
        value = int(input('input value: '))

        def fib(mode, value):
            try:
                if mode == 'i' and value >= 0:
                    if value == 0:
                        return value
                    elif value == 1:
                        return value
                    else:
                        return fib(mode, value - 1) + fib(mode, value - 2)
                elif mode == 'v' and value >= 0:
                    count = 1
                    while True:
                        fib_num = fib('i', count)
                        if fib_num < value:
                            count += 1
                        else:
                            if fib_num == value:
                                return f'{value} is in the sequence'
                            else:
                                return f'{value} is not in the sequence'
                else:
                    raise RuntimeError('Not a valid choice')
            except:
                print('Input a valid mode and value')
                mode = input('input mode (i, v): ')
                value = int(input('input value: '))
                ans = fib(mode, value)
                return ans

        ans = fib(mode, value)
        return ans
                    