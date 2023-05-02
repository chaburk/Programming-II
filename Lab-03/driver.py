from executive import Executive

'''
Author: Chase Burkdoll
KUID: 3082972
Date: 6/24/2022
Lab: lab3
Last Modified: 6/25/2022
Purpose: The driver.py file contains a main function that asks for an input file name and then takes the input to be run 
in the executive.py file through the use of the Executive class.
'''

def main():
    file_name = input("Enter the name of the input file: ")
    my_exec = Executive(file_name)
    my_exec.run()


if __name__ == '__main__':
    main()

"""
TO DO LIST:
documentation and docstings
"""