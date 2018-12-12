#get times when detectors detect the sound and return sector of sound direction
def direction(time1,time2,time3):
    times = [time1, time2, time3]
    #find the first detector to detect
    first = times.index(min(times))
    #last detector to detect
    last = times.index(max(times))
    
    #check first which sensor detected and then the last one
    if first == 0:        #left first
        if last == 1:      #mid last
            return '4'
        else:
            return '5'
    elif first == 1:       #center first
        if last == 2:      #rigt last
            return '6'
        else:
            return '1'   
    else:                   #right first
        if last == 0:       #left last
            return '2'
        else:
            return '3'