from executive import Executive

'''
Author: Chase Burkdoll
KUID: 3082972
Date: 7/15/2022
Lab: lab6
Last Modified: 7/20/2022
Purpose: The driver.py file contains a main function that runs an exec object.
'''

def main():
    input_file = input("Enter a file name: ")
    exec = Executive(input_file)
    exec.run()


if __name__ == "__main__":
    main()
    

"""
TO DO LIST:
DOCUMENTATION
"""