
# Disk Scheduling Algorithms

This repository contains implementations of six different disk scheduling algorithms in Python. The algorithms are:

    1. C-SCAN
    2. F-SCAN
    3. FIFO
    4. N-SCAN
    5. SCAN
    6. SSTF



Each algorithm is implemented as a separate Python script that takes a list of disk requests as input and returns the order in which the requests should be processed and every seek time corresponding to the process.


The output will be two lists the first list consists of integers representing the order in which the disk requests should be processed and the the second list consists of the seek time to each process in the same order of the processes list.



## Running 
```bash
py SCAN.py

requests : 176 79 34 60 92 11 41 114
enter current position : 50
(-) or (+) direction : -
num of cylinders : 200
################################################
request                 seek time
41                        9
34                        7
11                        23
0                         11
60                        60
79                        19
92                        13
114                       22
176                       62
################################################

total seek time =  226
```
```bash
py C-SCAN.py

requests : 98 183 41 122 14 124 65 67
enter current position : 53
(-) or (+) direction : +
num of cylinders : 200
################################################
request                 seek time
65                        12
67                        2
98                        31
122                       24
124                       2
183                       59
199                       16
0                         199
14                        14
41                        27
################################################

total seek time =  386
```
