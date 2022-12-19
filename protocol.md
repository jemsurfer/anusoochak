# Communication protocol for algorithms

__Input Protocol:__
A dictionary mapping Protocol to Arrival times and Burst Times of each processs

```python
inDict = {'Process1': [2,3], "Process2": [0,5]} 
```

Process1 has an Arrival TIme of 2ms and a Burst Time of 3ms. 
Process2 has an Arrrival Timme of 0ms and Burst Time of 5ms.


__Algorithmn Output Protocol:__
A dicitonary mapping Protocol to Start Times and End Times

```python
outDict = {"Process1": [[0,2],[4,6]], "Process2": [[2,4],[6,8]]}
```

Process1 has a Start time of 0ms then runs for 2ms for end of 2ms. Then starts again at 4ms and runs for 2ms for end of 6ms
Process2 has a Start time of 2ms then runs for 2ms for end of 4ms. Then starts again at 6ms and runs for 2ms for end of 8ms

__All algorithms need to use this protocol, to make ethan's job easier.__
