"""
 This module is for finding the execution time of a whole program

 It uses process_time() built-in function in python 3.7 or above
 More info on Docs : https://docs.python.org/3/library/time.html#time.process_time_ns

 Instruction:
    As soon as you import the module __name__ != '__main__' gets excuted and it is the starting of the program,\n
    (Prefer to import exeTime above all imports)

    ---Write your code---

    After finishing writing your code and successfully compilling,
        call exetime() or exetime_ms() [At the end of everything]
        (Use the print() for viewing the output)
"""

'''
----------------------------------------------------------
Credit: It was created by Saikat (https://github.com/saikat0326)
----------------------------------------------------------
'''


import time
import decimal

exeStart = 0.0

def exetime():
    '''
    returns total process-time for profiling as seconds:\n
    sum of kernel and User-space CPU time
    '''

    return (time.process_time_ns() - exeStart)/(10**9)

def exetime_ms():
    '''
    exetime() -> decimal

    Returns total process-time for profiling as milliseconds (ms):\n  sum of kernel and User-space CPU time
    '''

    return exetime()*1000

if __name__ != '__main__':
    exeStart =  decimal.Decimal(time.process_time_ns())

