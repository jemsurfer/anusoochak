class ShortTimeRemainingFirst:

    proc_a_w = [];
    n = 0;
    b_wt = 0;

    def __init__(self, n, processes):
        self.b_wt = [[0]*2]*n;
        self.n = n;
        self.proc_a_w = processes;

    def calc_b_wt(self):
        rt = []*self.n;


    def get_b_wt(self):
        self.b_wt = calc_b_wt();
        return self.b_wt;


"""
ShortestTimeRemaining first algorithmn
PAB = a dictionary of processes mapped to an array of arrival time, burst time
e.g {"Process1": [2,5]}
would be "Process1" with an arrival time of 5 milliseconds and burst time of 2 milliseconds.

Returns a 2d array where the first array contains a ProcessesID and the second array is start time and completion time
"""

def strf(pab):
