from complexity import Complexity

'''
Author: Chase Burkdoll
KUID: 3082972
Date: 7/1/2022
Lab: lab4
Last Modified: 7/6/2022
Purpose: The executive.py file contains an Executive class that has a user menu to call functions that display varying time complexity
problems.
'''

class Executive:
    def run(self):
        get_times = Complexity()
        print("""
        User Navigation
        1. Popping a single item from a stack
        2. Popping all items from a stack
        3. Queue's enqueue
        4. Linked List get_entry at index 0
        5. Linked List get_entry at the last index
        6. Printing all elements in a LinkeList using get_entry
        7. QUIT
        """)
        user_input = input('Which time do you want to see: ')
        while user_input  != '7':
            print("""
        User Navigation
        1. Popping a single item from a stack
        2. Popping all items from a stack
        3. Queue's enqueue
        4. Linked List get_entry at index 0
        5. Linked List get_entry at the last index
        6. Printing all elements in a LinkeList using get_entry
        7. QUIT
        """)
            if user_input == '1':
                get_times.pop_single_two()
                user_input = input('Which time do you want to see: ')
            elif user_input == '2':
                get_times.pop_all()
                user_input = input('Which time do you want to see: ')
            elif user_input == '3':
                get_times.enqueue_time()
                user_input = input('Which time do you want to see: ')
            elif user_input == '4':
                get_times.linked_list_zero()
                user_input = input('Which time do you want to see: ')
            elif user_input == '5':
                get_times.linked_list_end()
                user_input = input('Which time do you want to see: ')
            elif user_input == '6':
                get_times.linked_list_print()
                user_input = input('Which time do you want to see: ')
            elif user_input == '7':
                break