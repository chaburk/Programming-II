from cpu_scheduler import CPU_Scheduler

'''
Author: Chase Burkdoll
KUID: 3082972
Date: 6/17/2022
Lab: lab2
Last Modified: 6/22/2022
Purpose: The executive.py file contains a class that takes in a file_name and a run method that opens the input file and
splits it into a list of commands. After spliting the file into commands, the method iterates through the list and it sends the command to
a CPU_Scheduler class to handle the commands. 
'''

class Executive:
    def __init__(self, file_name):
        self._file_name = file_name

    def run(self):
        #Splits the input file into commands, instantiates a CPU_Scheduler object, and pass the commands to the CPU_Scheduler object
        input_file = open(str(self._file_name) + '.txt')
        commands = []
        for line in input_file:
            commands.append(line.split())

        cpu_scheduler = CPU_Scheduler()

        for line in commands:
            try:
                if line[0] == 'START':
                    cpu_scheduler.add_process(line[1])
                elif line[0] == 'CALL':
                    cpu_scheduler.call_process(line[1])
                elif line[0] == 'RETURN':
                    cpu_scheduler.return_process()
            except:
                print('Something went wrong')
