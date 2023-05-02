from executive import Executive

'''
Author: Chase Burkdoll
KUID: 3082972
Date: 6/10/2022
Lab: lab1
Last Modified: 6/14/2022
Purpose: The driver.py file contains a main function that asks for user input and then take the input to be run in the executive.py file
throught the user of the Executive class.
'''

def main():
    #Function that takes an input name and takes that info to the executive class to run our program.
    file_name = input("Enter the name of the input file: ")
    my_exec = Executive(file_name)
    print(my_exec.run())

    

if __name__ == "__main__":
    #verifies that the name of the function being ran is main
    main()


"""
Stuff to clean up but for the most part you are done!!!!!!
LETS GO

to do list:
2. Ask about the debugger and how to do the method thing

ask questions about if you do a getter do you need a setter or just convention
"""