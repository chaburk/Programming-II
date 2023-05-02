from executive import Executive

'''
Author: Chase Burkdoll
KUID: 3082972
Date: 7/22/2022
Lab: lab7
Last Modified: 7/24/2022
Purpose: The driver.py file contains a main function that asks for an input file name and then takes the input to be run 
in the executive.py file through the use of the Executive class.
'''

def main():
    input_file = input("What is the name of the file?: ")
    exec = Executive(input_file)
    exec.run()

if __name__ == "__main__":
    main()
