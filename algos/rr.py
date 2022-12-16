def rr(timeSlice, procDict):
    burstTimeArr = procDict['burst_times']
    for i in burstTimeArr:
        i -= timeSlice
        if i <= 0:
            pass
        else:
            burstTimeArr.append(i) 
