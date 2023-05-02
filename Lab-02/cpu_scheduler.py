from queue import Queue
from process import Process

'''
Author: Chase Burkdoll
KUID: 3082972
Date: 6/17/2022
Lab: lab2
Last Modified: 6/22/2022
Purpose: the cpu_scheduler.py file contains a class which contains a queue and the methods to perform the commands passed in by the 
executive class
'''

class CPU_Scheduler:
    def __init__(self):
        self._my_queue = Queue()

    def add_process(self, name):
        #Creates a Process object, adds main to the object's stack, and adds the Process to the queue.
        temp = Process(name)
        temp.add_to_stack('main')
        self._my_queue.enqueue(temp)
        print(name, 'added to queue')

    def call_process(self, name):
        #calls a function from the Process's stack and then adds the Process to the end of the Queue
        temp = self._my_queue.peek_front()
        print(temp.get_name(), 'calls', temp.add_to_stack(name))
        self._my_queue.dequeue()
        self._my_queue.enqueue(temp)

    def return_process(self):
        #Kills a Process if the only function on it's call stack is main, if another function of the call stack it calls then pops it off the stack
        temp = self._my_queue.peek_front()
        if temp.get_stack().peek() == 'main':
            print(temp.get_name(), 'returns from main')
            print(temp.get_name(), 'process has ended')
            self._my_queue.dequeue()
        else:
            self._my_queue.dequeue()
            print(temp.get_stack().pop(),'has ended')
            self._my_queue.enqueue(temp)