from inspect import stack
from queue import LinkedQueue
from stack import Stack
from linkedlist import LinkedList
import time

import xlwt
from xlwt import Workbook


'''
Author: Chase Burkdoll
KUID: 3082972
Date: 7/1/2022
Lab: lab4
Last Modified: 7/6/2022
Purpose: The complexity.py file contains 6 functions that test the time complexities of varying data structures and their methods.
'''


wb = Workbook()
sheet1 = wb.add_sheet('Sheet1')


class Complexity:
    def pop_single_two(self):
        #Creates a new stack and then fills with items to test time for popping one item at certain size
        for i in range(1,101):
            stacky = Stack()
            for j in range(i * 1000):
                stacky.push(j)
            start_time = time.perf_counter() 
            stacky.pop()
            end_time = time.perf_counter() 
            print("Total time to pop a single item off a stack of", i * 1000, 'items' ,end_time - start_time)
            #sheet1.write(i, 0, end_time - start_time)
        #wb.save('lab4excel.xls')

    def pop_all(self):
        #Creates a stack and then fills until the correct size and pops all items off
        stacky = Stack()
        for i in range(101000):
            stacky.push(i)
            if i % 1000 == 0 and i != 0:
                start_time = time.perf_counter()
                while stacky.is_empty() == False:
                    stacky.pop()
                end_time = time.perf_counter()
                for j in range(i):
                    stacky.push(j)
                print("Total time to pop", i ,'items off a stack', end_time - start_time)
                #sheet1.write(int(i/ 1000), 1, end_time - start_time)
        #wb.save('lab4excel.xls')

    def enqueue_time(self):
        #Creates a queue and times the time to enqueue a single item on different size queues
        queuey = LinkedQueue()
        for i in range(101000):
            queuey.enqueue(i)
            if i % 1000 == 0 and i != 0:
                start_time = time.perf_counter()
                queuey.enqueue(i)
                end_time = time.perf_counter()
                #sheet1.write(int(i/ 1000), 2, end_time - start_time)

                print("Total time to enqueue", i ,'items on a queue', end_time - start_time)
        #wb.save('lab4excel.xls')

    def linked_list_zero(self):
        #Creates a linked list and times the time to get the entry of the first index of varying size linked lists
        linkey_listy = LinkedList()
        for i in range(101000):
            linkey_listy.insert(0,i)
            if i % 1000 == 0 and i != 0:
                start_time = time.perf_counter()
                linkey_listy.get_entry(0)
                end_time = time.perf_counter()
                #sheet1.write(int(i/ 1000), 3, end_time - start_time)

                print('Total time to get entry at index 0 on a linked_list of', i , 'items' , end_time - start_time)
        #wb.save('lab4excel.xls')

    def linked_list_end(self):
        #Creates a linked list and times the time to get the entry of the last item of the linked list of varying sizes
        linkey_listy = LinkedList()
        for i in range(101000):
            linkey_listy.insert(0,i)
            if i % 1000 == 0 and i != 0:
                start_time = time.perf_counter()
                linkey_listy.get_entry(i)
                end_time = time.perf_counter()
                #sheet1.write(int(i/ 1000), 4, end_time - start_time)

                print('Total time to get entry at index', i ,'on a linked_list of', i , 'items' , end_time - start_time)
        #wb.save('lab4excel.xls')

    def linked_list_print(self):
        #Creates a linked list and times the time print all the entry of the linked list of varying sizes
        linkey_listy = LinkedList()
        for i in range(101000):
            linkey_listy.insert(0,i)
            if i % 1000 == 0 and i != 0:
                start_time = time.perf_counter()
                for j in range(i):
                    print(linkey_listy.get_entry(j))
                end_time = time.perf_counter()
                #sheet1.write(int(i/ 1000), 5, end_time - start_time)

                print('Total time to get print all etnires on a linked_list of', i , 'items' , end_time - start_time)
        #wb.save('lab4excel.xls')


            

    # def pop_single(self):
    #     stacky = Stack()
    #     for i in range(101000):
    #         stacky.push(i)
    #         if i % 1000 == 0 and i != 0:
    #             start_time = time.perf_counter_ns() 
    #             stacky.pop()
    #             end_time = time.perf_counter_ns()
    #             print("Total time to pop a single item off a stack of", i, 'items' ,end_time - start_time)

    
