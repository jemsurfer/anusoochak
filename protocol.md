# Communication protocol for algorithms

__Input Protocol:__
A dictionary mapping Protocol to Arrival times and Burst Times of each processs

```python
inDict = {'Process1': [2,3], "Process2": [0,5]} 
```

Process1 has an Arrival Time of 2ms and a Burst Time of 3ms. 
Process2 has an Arrival Time of 0ms and Burst Time of 5ms.


__Algorithmn Output Protocol:__
A dictionary mapping Protocol to Start Times and End Times

```python
outDict = {"Process1": [[0,2],[4,6]], "Process2": [[2,4],[6,8]]}
```
The first index of the array is the arrival times, and the second is the end times.

__All algorithms need to use this protocol, to make ethan's job easier.__
