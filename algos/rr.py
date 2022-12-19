def rr(procDict):
    quantum = 2 #Timeslice of 2ms
    numberOfCycles = 0 #Number of times the process has executed for a whole quantum
    outDict = {}
    for i in procDict:
        arrivalTime = procDict[i][0]
        remainingTime = procDict[i][1] #Remaining time starts as the burst time
        if remainingTime <= quantum: #If the process takes less than the quantum don't do checks
            timeTaken = arrivalTime+remainingTime
            outDict[i] = [[arrivalTime],[timeTaken]]#Return 2d array with arrival and completion times
        else:
            remainingTime -= quantum #Subtract timeslice from remaining time. 
            numberOfCycles += 1
            outDict[i][0].append(numberOfCycles*quantum)
            if remainingTime < 0: # If the process is done stop executing
                pass
            else: #Else put the process back to the back of the queue
                procDict[0] = procDict[i] 
    return outDict

if __name__=='__main__':
    print("Input the processes, their start times, and burst times in the format proc1 10 10, where the 1st number is the start time, and the 2nd is the burst time.")
