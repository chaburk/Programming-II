from executive import Executive

'''
Author: Chase Burkdoll
KUID: 3082972
Date: 6/17/2022
Lab: lab2
Last Modified: 6/22/2022
Purpose: The driver.py file contains a main function that asks for an input file name and then takes the input to be run 
in the executive.py file through the use of the Executive class.
'''

def main():
    #function takes in a user input and runs a Executive method
    file_name = input("Enter the name of the input file: ")
    my_exec = Executive(file_name)
    try:
        my_exec.run()
    except:
        print('File input was not found')

if __name__ == "__main__":
    #makes sure the function being ran is main
    main()
