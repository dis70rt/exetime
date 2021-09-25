# exetime 3.7

This module is for finding the execution time of a whole program
## Contents:
* [General Information](https://github.com/saikat0326/exetime#general-information)
* [Instruction](https://github.com/saikat0326/exetime#instruction)
    * Example-1
    * Example-2
* [Developer and Credits](https://github.com/saikat0326/exetime#developer-and-credits)

# General Information:
It uses process_time() built-in function in ***python 3.7*** or above.
More info on  [Python Docs](https://docs.python.org/3/library/time.html#time.process_time_ns)

# Instruction:
     
   As soon as you import the module,
   __init__() gets excuted and it is the starting of the program,
   >(Prefer to import exeTime above all imports)

   ---Write your code---

   After finishing writing your code and successfully compilling,
       call `exetime()` or `exetime_ms()` (At the end of everything)
  >Use the `print()` for viewing the output

 ### Example-1:
    import exetime
    # Your Other
    # Imports here
 
    # Write some code
 
    print(exetime.exetime())
 
 ### Example-2:
    import exetime
    import time
    
    sum = 0
    for x in range(100000):
        sum = sum + x
    time.sleep(5)
    
    print(exetime.exetime())
   
**Note:** the delay of `time.sleep(5)` won't be included, since it only calculate the process time by CPU

# Developer and Credit
This module was developed by Saikat
* [Website](https://saikat.in)
* [Instagram](https://instagram.com/saikat._)
* [Twitter](https://twitter.com/SaikatDas_)

External Credit:
* [StackOverFlow Question](https://stackoverflow.com/a/1557584/12404738)
* [Marc Maxmeister](https://stackoverflow.com/users/536538/marc-maxmeister)
    
    
