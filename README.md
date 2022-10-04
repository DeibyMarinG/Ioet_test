# Ioet_test

Sample test for Ioet.

This application has the purpouse of getting the workdays of some workers, inside a textfile on the following style:

**WORKER_NAME=MO13:00-16:00,SU01:00-09:00**

If a line is not set  properly, it raises an exception and the programm continues with another line.

For use of apllication use command. where filename is the name of your file:

**python main.py filename.txt**

or

**python3 main.py filename.txt**

If a filename is not given, it raises an exception.


The aplicattion uses a class named worker, wich has te following methods:

    __init__(self, line): Recieves the single line from a file reading

    calc(self): Divides the line of days and return the total_money

    obtain_time(self,code_time): Obtain the datetime objects of the string line

    treat_order(self,code, money=0): Treat day by day of a worker

    process_time(self,day): Calculate the number of worked hours and the pay of a day

    __str__(self): Gives a string formatted information of the worker



Tested on python 3.9.2
