from linkedlist import LinkedList

'''
Author: Chase Burkdoll
KUID: 3082972
Date: 6/24/2022
Lab: lab3
Last Modified: 6/25/2022
Purpose: The browser.py file contains a Browser class that contains a LinkedList and uses methods to simulate a web browser.
'''

class Browser:
    def __init__(self):
        self._my_list = LinkedList()
        self.current_index = 0

    def navigate_to(self, url):
        #Method adds websites to _my_list and makes it the current running website. 
        if self._my_list.length() == 0:
            self._my_list.insert(self._my_list.length(), url)
        elif self.current_index != self._my_list.length() - 1:
            for i in range(self._my_list.length()- 1, self.current_index, -1):
                self._my_list.remove(i)
            self._my_list.insert(self._my_list.length(), url)
            self.current_index += 1
        else:
            self._my_list.insert(self._my_list.length(), url)
            self.current_index += 1

    def forward(self):
        #Method increases the current_index which tells us what website we are on
        if self.current_index < self._my_list.length()- 1:
            self.current_index += 1

    def back(self):
        #Method decreases the current_index which tells us what website we are on
        if self.current_index > 0:
            self.current_index -= 1

    def history(self):
        #Method prints the history and where you currently are on the browser
        print('Oldest')
        print('===========')
        for i in range(self._my_list.length()):
            if i == self.current_index:
                print(self._my_list.get_entry(i) + '    <==current')
            else:
                print(self._my_list.get_entry(i))
        print('===========')
        print('Newest')
        print()

